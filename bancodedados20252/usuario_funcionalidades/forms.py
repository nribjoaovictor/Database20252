from django import forms
from .models import Solicitacoleta

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacoleta
        fields = ['descricao', 'tipagem_residuo']
        
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tipagem_residuo': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'descricao': 'Descrição da Solicitação',
            'tipagem_residuo': 'Tipo do Resíduo'
        }