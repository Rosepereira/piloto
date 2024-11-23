from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

def exibir_item(request,id):
    return render(request,'exibir_item.html', {'id':id})

def perfil(request,usuario):
    return render(request,'perfil.html', {usuario:'Rosemary da Silva'})

def diasemana(request, numero):

    dias = {
        1: "domingo",
        2: "segunda-feira",
        3: "terça-feira",
        4: "quarta-feira",
        5: "quinta-feira",
        6: "sexta-feira",
        7: "sábado"
    }
    if numero in dias:
        dia = dias[numero]
        return HttpResponse(f'O dia passado corresponde a {dia}.')
    else:
        return HttpResponse("O dia passado corresponde a dia inválido.")
    