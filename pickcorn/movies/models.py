from django.db import models
from django.conf import settings

# class Genres(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=30)


class Movie(models.Model):
    # 디폴트인 id 생성하지 않음
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    overview = models.TextField()
    # ipynb genres -> 파싱 -> dict
    # genre 모델화
    genres = models.TextField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    # 좋아요 한 영화
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # genres = models.ManyToManyField(Genres)


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)