from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html', {'title':'Página Principal' ,'message':'Página Principal'})

def sobre(request):
    return render(request,'sobre.html', {'title': 'Sobre', 'message': 'Sobre', 'user_name':''})

def contato(request):
    return render(request,'contato.html', {'title':'Contato', 'message':'Contato','user_name':'' })
