from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Empresa, Funcionario, Solicitacoleta
from .forms import SolicitacaoForm  
from datetime import date
from django.db import IntegrityError


def login_usuario(request):  
    if request.method == 'POST':
        login_post = request.POST.get('login')
        senha_post = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(login=login_post, senha=senha_post)
            
            empresa = Empresa.objects.filter(fk_usuario=usuario).first()
            funcionario = Funcionario.objects.filter(fk_usuario=usuario).first()

            request.session['usuario_id'] = usuario.id

            if empresa:
                request.session['perfil'] = 'empresa'
                request.session['entidade_id'] = empresa.id
                return redirect('listar_chamados')
            
            elif funcionario:
                request.session['perfil'] = 'funcionario'
                request.session['entidade_id'] = funcionario.id
                return redirect('painel_funcionario') 
            
            else:
                messages.error(request, 'Usuário sem perfil vinculado.')

        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'tela_login.html')

def logout_usuario(request):
    request.session.flush()
    return redirect('login')


def listar_chamados(request):
    if request.session.get('perfil') != 'empresa':
        return redirect('login')

    empresa_id = request.session.get('entidade_id')
    
    chamados = Solicitacoleta.objects.filter(fk_empresa_id=empresa_id)
    
    empresa = Empresa.objects.get(id=empresa_id)
    
    return render(request, 'lista.html', {'chamados': chamados, 'empresa': empresa})

def criar_chamado(request):
    if request.session.get('perfil') != 'empresa': return redirect('login')

    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False)
            
            chamado.fk_empresa_id = request.session['entidade_id'] # Vincula à empresa logada
            chamado.data_abertura = date.today()
            chamado.status = 'Aberto'
            
            chamado.save()
            messages.success(request, "Solicitação aberta com sucesso!")
            return redirect('listar_chamados')
    else:
        form = SolicitacaoForm()

    return render(request, 'form.html', {'form': form, 'titulo': 'Nova Coleta'})

def editar_chamado(request, id):
    if request.session.get('perfil') != 'empresa': return redirect('login')
    
    empresa_id = request.session.get('entidade_id')
    chamado = get_object_or_404(Solicitacoleta, id=id, fk_empresa_id=empresa_id)

    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect('listar_chamados')
    else:
        form = SolicitacaoForm(instance=chamado)

    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Solicitação'})

def excluir_chamado(request, id):
    if request.session.get('perfil') != 'empresa': 
        return redirect('login')
    
    empresa_id = request.session.get('entidade_id')
    chamado = get_object_or_404(Solicitacoleta, id=id, fk_empresa_id=empresa_id)
    
    if chamado.status != 'Aberto':
        messages.error(request, "Você não pode excluir uma solicitação que já foi aprovada ou está em andamento.")
        return redirect('listar_chamados')

    if request.method == 'POST':
        try:
            chamado.delete()
            messages.success(request, "Solicitação excluída com sucesso!")
            return redirect('listar_chamados')
            
        except IntegrityError:
            messages.error(request, "Erro: Existem registros vinculados a este chamado no sistema.")
            return render(request, 'confirm_delete.html', {'chamado': chamado})

    return render(request, 'confirm_delete.html', {'chamado': chamado})