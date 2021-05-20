from django.core import serializers
from .serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Movie, Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import JsonResponse, HttpResponse

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
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    articles = movie.article_set.all()
    article_form = ArticleForm(request.POST)
    context = {
        'movie': movie,
        'articles': articles,
        'article_form': article_form,
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
            return redirect('movies:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/article_create.html', context)


@require_GET
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
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
        return redirect('movies:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': article.comment_set.all(),
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            liked=False
        else:
            article.like_users.add(user)
            liked=True

        response_data = {
            'liked': liked,
            'count': article.like_users.count()
        }
        
        return JsonResponse(response_data)
    return HttpResponse(status=401)



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
    
    

