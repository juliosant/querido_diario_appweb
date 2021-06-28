from .models import Diario
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .form import LoginForm, DiarioForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def criar_usuario(request):
    if request.POST:
        usuario_form = UserCreationForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('login')
    
    usuario_form = UserCreationForm()
    context = {
        'usuario_form': usuario_form
    }
    return render(request, 'usuario/create_user.html', context)


def fazer_login(request):
    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['usuario'], password=cd['senha'])
            if user is not None:
                login(request, user)
                return redirect("list")
            else:
                return HttpResponse("<h1>Usuário ou senha inválidos</h1>")

    login_form = LoginForm()
    context = {
        'form':login_form
    }
    return render(request, 'usuario/login.html', context)


def fazer_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def informacoes_usuario(request):
    diario_qtd = Diario.objects.filter(usuario=request.user).count()
    context = {
        'diario_qtd': diario_qtd
    }
    return render(request, 'diario/user_info.html', context)


@login_required(login_url='login')
def listar_diario(request):
    diaries = Diario.objects.filter(usuario=request.user)
    context = {
        'diaries': diaries
    }
    return render(request, 'diario/diary_list.html', context)


@login_required(login_url='login')
def criar_diarios(request):
    if request.POST:
        diary_form = DiarioForm(request.POST)
        if diary_form.is_valid():
            form = diary_form.save(commit=False)
            form.usuario = request.user
            form.save()
            return redirect('list')

    diary_form = DiarioForm()
    context = {
        'diary_form': diary_form
    }

    return render(request, 'diario/create_diary.html',  context)


@login_required(login_url='login')
def excluir_diario(request, id):
    print(type(id))
    diary = Diario.objects.get(id=id).delete()
    return redirect('list')


@login_required(login_url='login')
def alterar_diario(request, id):
    diary = Diario.objects.get(id=id)
    diary_form = DiarioForm(instance=diary)
    if request.POST:
        form = DiarioForm(request.POST, instance=diary)
        if form.is_valid():
            form.usuario = request.user
            form.save()
            return redirect('list')
    
    context = {
        'diary_form': diary_form
    }
    print('a')
    return render(request, 'diario/update_diary.html', context)
