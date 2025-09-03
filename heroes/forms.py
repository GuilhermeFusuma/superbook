from django import forms
from .models import DimHero

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Seu nome")
    email = forms.EmailField(required=True, label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea, required=True)

class HeroForm(forms.ModelForm):
    class Meta:
        model = DimHero
        fields = ['code_name', 'real_name', 'power', 'city', 'history']
                  
