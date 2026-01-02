from django.shortcuts import render

# Create your views here.

def landpage(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        enviado = 'Formulário enviado com sucesso!' 
        return render(request, 'landpage.html', context={'enviado': enviado})
    
    return render(request, 'landpage.html')
    
    

    
