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



# 회원가입
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            '''
            # 👉 회원가입 / 로그인 페이지를 bootstrap 외부 템플릿으로 이용했기 때문에 기존 코드와 방식이 다름
            user = form.save()    
            '''
            form.save()
            username = form.cleaned_data.get('username')
            # 👉사용자가 정한 아이디(username)

            raw_password = form.cleaned_data.get('password1')
            # 👉 사용자가 정한 비밀번호(password1) / password2 : 비밀번호 확인

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



# 로그인
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



# 로그아웃
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


# 개인 프로필
@require_GET
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    rated_good_movies = person.rated_good_movies.all()
    like_movies = person.like_movies.all()

    # paginator를 통해 6개씩 페이지를 나눠서 받아옴
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


# 타 유저 follow 기능
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


# 유저의 following 명단
def followings(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'person': person,
    }
    return render(request, 'accounts/followings.html', context)


# 유저의 follower 명단
def followers(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'person': person,
    }
    return render(request, 'accounts/followers.html', context)