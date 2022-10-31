from django.shortcuts import render

from .models import Pessoa


# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request , 'index.html', {'pessoas' : pessoas})

def salvar(request):
    var_nome = request.POST.get('nome')
    Pessoa.objects.create(nome=var_nome)
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas' : pessoas})

