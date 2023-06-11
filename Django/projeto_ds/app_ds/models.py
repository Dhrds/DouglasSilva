from django.db import models

class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nome
