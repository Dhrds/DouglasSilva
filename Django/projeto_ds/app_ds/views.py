from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User

def home(request):
    return render(request,'usuarios/home.html')

def cadastro(request):
    novo_usuario = Usuario()
    if request.method == "GET":
        usuarios = {
            'usuarios':Usuario.objects.all()
        }
        return render(request,'usuarios/usuarios.html',usuarios)
    else:
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()
        usuarios = {
            'usuarios':Usuario.objects.all()
        }
        return render(request,'usuarios/usuarios.html',usuarios)