from django import forms
from .models import FactPost

class PostForm(forms.ModelForm):
    class Meta:
        model = FactPost
        fields = ['author', 'message', 'image']
