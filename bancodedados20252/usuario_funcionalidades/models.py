from django.db import models

class Autorizacao(models.Model):
    status = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    fk_coleta = models.ForeignKey('Coleta', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autorizacao'


class Bairro(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    fk_cidade = models.ForeignKey('Cidade', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bairro'


class Cidade(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    fk_estado = models.ForeignKey('Estado', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cidade'


class Coleta(models.Model):
    data_inicio = models.DateField(blank=True, null=True)
    data_termino = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    quantidade_residuo = models.FloatField(blank=True, null=True)
    fk_solicitacoleta = models.ForeignKey('Solicitacoleta', models.DO_NOTHING, blank=True, null=True)
    fk_residuo = models.ForeignKey('Residuo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coleta'


class Email(models.Model):
    email = models.CharField(max_length=150, blank=True, null=True)
    fk_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'


class Empresa(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    nomefantasia = models.CharField(max_length=150, blank=True, null=True)
    cnpj = models.CharField(unique=True, max_length=20, blank=True, null=True)
    fk_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Empresaterc(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    cnpj = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresaterc'


class EmpresatercColeta(models.Model):
    fk_coleta = models.ForeignKey(Coleta, models.DO_NOTHING, blank=True, null=True)
    fk_empresaterc = models.ForeignKey(Empresaterc, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresaterc_coleta'


class Endereco(models.Model):
    fk_logradouro = models.ForeignKey('Logradouro', models.DO_NOTHING, blank=True, null=True)
    fk_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereco'


class Estado(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Funcionario(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=14, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    fk_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcionario'


class FuncionarioColeta(models.Model):
    fk_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, blank=True, null=True)
    fk_coleta = models.ForeignKey(Coleta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcionario_coleta'


class Licenca(models.Model):
    numero = models.CharField(max_length=50, blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    data_validade = models.DateField(blank=True, null=True)
    fk_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licenca'


class Logradouro(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    fk_bairro = models.ForeignKey(Bairro, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logradouro'


class Orgaoambiental(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    sigla = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgaoambiental'


class OrgaoambientalLicenca(models.Model):
    fk_orgaoambiental = models.ForeignKey(Orgaoambiental, models.DO_NOTHING, blank=True, null=True)
    fk_licenca = models.ForeignKey(Licenca, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgaoambiental_licenca'


class Residuo(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'residuo'


class Solicitacoleta(models.Model):
    data_abertura = models.DateField(blank=True, null=True)
    data_fechamento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    fk_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    
    descricao = models.TextField(null=True, blank=True)
    
    TIPO_CHOICE = [('L','Liquido'),('G','Gasoso'),('S','Sólido')]
    tipagem_residuo = models.CharField(max_length=1, choices=TIPO_CHOICE, default='S')

    class Meta:
        managed = True  
        db_table = 'solicitacoleta'


class Telefone(models.Model):
    telefone = models.CharField(max_length=20, blank=True, null=True)
    fk_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefone'


class Usuario(models.Model):
    # ATENÇÃO: Essa é a tabela Usuario do seu banco legado, não a do Django.
    login = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    ultimo_acesso = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Veiculo(models.Model):
    placa = models.CharField(unique=True, max_length=20, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo'


class VeiculoColetaFuncionario(models.Model):
    fk_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, blank=True, null=True)
    fk_veiculo = models.ForeignKey(Veiculo, models.DO_NOTHING, blank=True, null=True)
    fk_coleta = models.ForeignKey(Coleta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_coleta_funcionario'


class VeiculoResiduo(models.Model):
    fk_veiculo = models.ForeignKey(Veiculo, models.DO_NOTHING, blank=True, null=True)
    fk_residuo = models.ForeignKey(Residuo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_residuo'