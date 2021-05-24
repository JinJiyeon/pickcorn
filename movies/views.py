from django.core import serializers
# from .serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Movie, Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
import random

# , Comment, Article
# from .serializers import (MovieSerializer, 
#                         MovieListSerializer, 
#                         CommentSerializer, 
#                         CommentListSerializer, 
#                         ArticleSerializer,
#                         ArticleListSerializer,
# )
# Create your views here.

def recommend(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    data = serializers.serialize('json', [movie])
    context = {
        'data': data
    }
    return render(request, 'movies/recommend.html', context)

@require_GET
def index(request):
    weighted_vote_movies = Movie.objects.order_by('-weighted_vote')[:5]
    vote_movies = Movie.objects.order_by('-vote_count')[:5]
    movies = list(Movie.objects.all())
    random_movies = random.sample(movies, 5)
    
    # 로그인 한 회원일 시
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=request.user.pk)
        

        # 유저의 플레이리스트 기반 추천
        playlist = list(person.like_movies.all())
        playlist_recom = []

        if (len(playlist) > 2):
            while len(playlist_recom) < 10:
                for play in playlist:
                    playlist_recom += list(play.recommends.all())

                # 중복 제거
            playlist_recom_set = set(playlist_recom)
            playlist_recom = list(playlist_recom_set)

            playlist_recom = random.sample(playlist_recom, 5)

        # 팔로우 한 사람의 플레이리스트 기반 추천
        followingslist = []
        for following in person.followings.all():
            followingslist += list(following.like_movies.all())
        
        if (len(followingslist) > 0) and (len(followingslist) < 10):
            while len(followingslist) < 10:
                add_recom = []
                for following in followingslist:
                    add_recom += list(following.recommends.all())
                followingslist += add_recom
            
            followingslist_set = set(followingslist)
            followingslist = list(followingslist_set)

            followingslist = random.sample(followingslist, 5) 

            context = {
            'weighted_vote_movies': weighted_vote_movies,
            'vote_movies': vote_movies,
            'person': person,
            'followingslist': followingslist,
            'playlist_recom': playlist_recom,
            'random_movies': random_movies,
            }
        else: 
            context = {
            'weighted_vote_movies': weighted_vote_movies,
            'vote_movies': vote_movies,
            'person': person,
            'playlist_recom': playlist_recom,
            'random_movies': random_movies,
            }

    else:
        context = {
            'weighted_vote_movies': weighted_vote_movies,
            'vote_movies': vote_movies,
            'random_movies': random_movies,
        }
    


    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    articles = movie.article_set.all()
    
    context = {
        'movie': movie,
        'articles': articles,
        
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def article_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.movie = movie
            article.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/article_create.html', context)


def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    movie = get_object_or_404(Movie, pk=article.movie_id)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.movie = movie
                article.save()
                return redirect('movies:article_detail', article.pk)
        else:
            form = ArticleForm(instance = article)
        context = {
            'form': form,
            'movie': movie,
        }
        return render(request, 'movies/article_update.html', context)

    return redirect('movies:detail', movie.pk)


def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    movie = get_object_or_404(Movie, pk=article.movie_id)
    if request.user == article.user:
        article.delete()
    return redirect('movies:detail', movie.pk)


@require_GET
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    movie = get_object_or_404(Movie, pk=article.movie_id)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
        'movie': movie,
    }
    return render(request, 'movies/article_detail.html', context)


@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('movies:article_detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': article.comment_set.all(),
    }
    return render(request, 'movies/detail.html', context)


def delete_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = get_object_or_404(Article, pk=comment.article_id)
    if request.user == comment.user:
        comment.delete()
    
    return redirect('movies:article_detail', article.pk)

@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            liked=False
        else:
            movie.like_users.add(user)
            liked=True

        response_data = {
            'liked': liked,
            'count': movie.like_users.count()
        }
        
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')


def rate_good(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.rated_good_users.filter(pk=user.pk).exists():
            movie.rated_good_users.remove(user)
            rated_good=False
        else:
            movie.rated_good_users.add(user)
            rated_good=True
            if movie.rated_bad_users.filter(pk=user.pk).exists():
                movie.rated_bad_users.remove(user)
                rated_bad=False

        response_data = {
            'rated_good': rated_good,
            'rated_good_count': movie.rated_good_users.count()
        }
        
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')

def rate_bad(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.rated_bad_users.filter(pk=user.pk).exists():
            movie.rated_bad_users.remove(user)
            rated_bad=False
        else:
            movie.rated_bad_users.add(user)
            rated_bad=True
            if movie.rated_good_users.filter(pk=user.pk).exists():
                movie.rated_good_users.remove(user)
                rated_good=False

        response_data = {
            'rated_bad': rated_bad,
            'rated_bad_count': movie.rated_bad_users.count()
        }
        
        return redirect('movies:detail', movie.pk)

    return redirect('accounts:login')

# @api_view(['GET','POST'])
# def movie_articles(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     if request.method == 'GET':
#         article_list = movie.article_set.all()
#         serializer = ArticleSerializer(article_list, many=True)
#         return Response(serializer.data)
#     else: # POST
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(movie=movie)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET','PUT','DELETE'])
# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
    
#     else:
#         article.delete()
#         response = {'pk':pk}
#         return Response(response, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def comments(request):
# # Comment 목록을 가져온다, 없으면 404를 응답한다.
#     comments_list = get_list_or_404(Comment)
#     serializer = CommentListSerializer(comments_list, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def comment_detail(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     serializer = CommentSerializer(comment)
#     return Response(serializer.data)
    

# @api_view(['GET', 'POST'])
# def article_comments(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     if request.method == 'GET':
#         comment_list = article.comment_set.all()
#         serializer = CommentSerializer(comment_list, many=True)
#         return Response(serializer.data)
    
#     else:
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(article=article)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    

