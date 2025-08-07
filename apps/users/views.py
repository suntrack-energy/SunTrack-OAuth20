from django.shortcuts import render, redirect
from apps.users.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()
    next_url = request.GET.get('next') or request.POST.get('next')  # <-- importante!

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email_login = form['email_login'].value()
            senha_login = form['senha_login'].value()

            usuario = auth.authenticate(
                request,
                username=email_login,
                password=senha_login,
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, 'Usuário logado com sucesso!')
                
                if next_url:
                    return redirect(next_url)
                return redirect('index')
            
            else:
                messages.error(request, 'Erro ao efetuar o Login.')
                return redirect('login')
        
    return render(request, 'users/login.html', {'form': form, 'next': next_url})

def cadastrar(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome_cadastro = form['nome_cadastro'].value()
            sobrenome_cadastro = form['sobrenome_cadastro'].value()
            email_cadastro = form['email_cadastro'].value()
            senha_cadastro = form['senha1_cadastro'].value()

            if User.objects.filter(email=email_cadastro).exists():
                messages.error(request, 'Já existe um e-mail cadastrado com esses dados!')
                return redirect('cadastrar')

            usuario = User.objects.create_user(
                username=email_cadastro,
                first_name=nome_cadastro,
                last_name=sobrenome_cadastro,
                email=email_cadastro,
                password=senha_cadastro,
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
    
    return render(request, 'users/cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
