from django.shortcuts import render
from django.http import HttpResponse
from .models import Contato
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Contato

# Create your views here.

def landpage(request):

    if request.method == 'POST':

        # Recuperando os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        enviado = 'Formulário enviado com sucesso!' 

        # Salvando os dados no banco de dados
        contato = Contato(nome=nome, email=email, mensagem=mensagem)
        contato.save()

        return render(request, 'landpage.html', context={'enviado': enviado})
    
    return render(request, 'landpage.html')

@login_required(login_url='login')  # Redireciona para a rota 'login' se não autenticado
def painel_mensagens(request):
    mensagens = Contato.objects.all().order_by('-data_envio')
    return render(request, 'painel.html', {'mensagens': mensagens})
    
    

    
