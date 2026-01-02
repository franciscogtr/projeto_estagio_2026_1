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
    
    

    
