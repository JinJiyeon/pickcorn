from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import CustomUserCreationForm
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator



# νμκ°μ
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            '''
            # π νμκ°μ / λ‘κ·ΈμΈ νμ΄μ§λ₯Ό bootstrap μΈλΆ ννλ¦ΏμΌλ‘ μ΄μ©νκΈ° λλ¬Έμ κΈ°μ‘΄ μ½λμ λ°©μμ΄ λ€λ¦
            user = form.save()    
            '''
            form.save()
            username = form.cleaned_data.get('username')
            # πμ¬μ©μκ° μ ν μμ΄λ(username)

            raw_password = form.cleaned_data.get('password1')
            # π μ¬μ©μκ° μ ν λΉλ°λ²νΈ(password1) / password2 : λΉλ°λ²νΈ νμΈ

            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            # return redirect('movies:index')
            return render(request, 'accounts/signupload.html')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)



# λ‘κ·ΈμΈ
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            print(request.GET.get('next'))
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)



# λ‘κ·Έμμ
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


# κ°μΈ νλ‘ν
@require_GET
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    rated_good_movies = person.rated_good_movies.all()
    like_movies = person.like_movies.all()

    # paginatorλ₯Ό ν΅ν΄ 6κ°μ© νμ΄μ§λ₯Ό λλ μ λ°μμ΄
    paginator = Paginator(rated_good_movies, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    like_paginator = Paginator(like_movies, 6)
    like_page = request.GET.get('like_page')
    like_posts = like_paginator.get_page(like_page)    

    context = {
        'person': person,
        'posts': posts,
        'like_posts': like_posts,
        'page':like_page
    }
    return render(request, 'accounts/profile.html', context)


# ν μ μ  follow κΈ°λ₯
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if request.user != person:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.pk)
    else:
        return redirect('accounts:login')


# μ μ μ following λͺλ¨
def followings(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'person': person,
    }
    return render(request, 'accounts/followings.html', context)


# μ μ μ follower λͺλ¨
def followers(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'person': person,
    }
    return render(request, 'accounts/followers.html', context)