from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['autor', 'mensagem', 'imagem']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Itera sobre todos os campos do formulário
        for field_name, field in self.fields.items():
            # Adiciona a classe 'form-control' a cada um deles
            field.widget.attrs['class'] = 'form-control'