from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Lembrete
from .forms import LembreteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


@login_required
def index(request):
    """
        Filtra as permissões e as postagens para exibição na home.
        retorna pagina com as publicações.
    """
    
    dados = {}
    # # Esse trecho filtra a permissão do usuario logado
    # permissao = Group.objects.filter(user = request.user)
    
    # # Trata a permisão para exibir no front
    # for perm in permissao:
    #     permissao = str(perm)
    
    # # Se o usurio não estiver com nenhum grupo de permissão atribuido por padrão exibira Usuario
    # if str(permissao) == '<QuerySet []>':
    #     permissao = 'Usuario'
    
    # Filtra a publicações por usuario
    dados['lembretes'] = Lembrete.objects.filter(author=request.user)
    # Passa a permissão para o front
    # dados['permissao'] = permissao
    
    # # Depedendo da permissão e possivel ver todas as publicações
    # if permissao == 'Supervisor' or permissao == 'Admin':
    #     dados['lembretes'] = Lembrete.objects.all()
    
    return render(request, 'index.html', dados)


@login_required
def new(request):
    """
        Filtra a permissão, passa o formulario e os salva no banco de dados.
    """
    
    # permissao = Group.objects.filter(user = request.user)
    # for perm in permissao:
    #     permissao = str(perm)
    
    # if str(permissao) == '<QuerySet []>':
    #     permissao = 'Usuario'
    
    # if permissao == 'Supervisor':
    #     return redirect('index')
    
    dados = {}
    form = LembreteForm(request.POST or None)
    
    if form.is_valid():
        
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        
        return redirect('index')
    
    dados['form'] = form
    # dados['permissao'] = permissao
    return render(request, 'new.html', dados)
    


@login_required
def update(request, id: int):
    """
        Recebe o id do lembrete e faz alterações.
    """
    
    # permissao = Group.objects.filter(user = request.user)
    # for perm in permissao:
    #     permissao = str(perm)
    
    # if str(permissao) == '<QuerySet []>':
    #     permissao = 'Usuario'
    
    # if permissao == 'Supervisor':
    #     return redirect('index')
    
    dados = {}
    lembrete = Lembrete.objects.get(id=id)
    form = LembreteForm(request.POST or None, instance=lembrete)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('index')

    dados['form'] = form
    # dados['permissao'] = permissao
    return render(request, 'new.html', dados)


@login_required
def delete(request, id: int):
    """
        Deleta a publicação baseada no id, com confirmação.
    """
    
    data = {}
    # permissao = Group.objects.filter(user = request.user)
    # for perm in permissao:
    #     permissao = str(perm)
    
    # if permissao == 'Supervisor':
    #     return redirect('index')
    
    lembrete = Lembrete.objects.filter(author = request.user)
    lembrete = get_object_or_404(lembrete, id = id)
    
    if request.method == 'POST':
        lembrete.delete()
        return redirect('index')
    
    data['lembrete'] = lembrete
    return render(request, 'delete_confirm.html', data)


def signup(request):
    """
        Pagina de cadastro para novos usuario.
    """
    
    data = {}
    form = UserCreationForm(request.POST or None)
    data['form'] = form
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
        return redirect('login')
    
    return render(request, 'registration/signup.html', data)


@login_required
def logout_page(request):
    """
        Desloga o usuario
    """
    
    logout(request)
    return redirect('login')
