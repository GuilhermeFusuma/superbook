from django import forms
from .models import Hero

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Seu nome")
    email = forms.EmailField(required=True, label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea, required=True)

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['imagem', 'codinome', 'nome_real', 'poder', 'cidade', 'historia']
                  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Itera sobre todos os campos do formulário
        for field_name, field in self.fields.items():
            # Adiciona a classe 'form-control' a cada um deles
            field.widget.attrs['class'] = 'form-control'