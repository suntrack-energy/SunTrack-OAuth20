from django.shortcuts import render, get_object_or_404, redirect
from apps.suntrack.models import Servicos
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from urllib.parse import urlencode

def index(request):
    servicos = Servicos.objects.filter(publicada=True)

    return render(request, 'suntrack-energy/index.html')

@login_required
def servico(request, imagem_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue o Login para continuar')
        query_string = urlencode({'next':request.path})
        return redirect(f'/login?{query_string}')
    
    servicos = get_object_or_404(Servicos, pk=imagem_id) # pk -> Primary Key

    return render(request, 'suntrack-energy/servico.html', {'servicos': servicos})

def buscar(request):
    servicos = Servicos.objects.filter(publicada=True)

    if 'buscar' in request.GET:
        titulo_a_buscar = request.GET['buscar']
        if titulo_a_buscar:
            servicos = servicos.filter(titulo__icontains=titulo_a_buscar)

    return render(request, 'suntrack-energy/index.html', {'cards': servicos})