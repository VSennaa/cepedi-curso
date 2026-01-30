from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    matriculado = models.BooleanField(default=True)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome