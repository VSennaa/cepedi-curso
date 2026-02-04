from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
<<<<<<< HEAD
        fields = ['nome', 'idade', 'email', 'matriculado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
=======
        fields = ['nome', 'idade', 'email', 'matriculado']
>>>>>>> voltando
