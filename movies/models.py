from django.db import models
from django.conf import settings

# Genre 필드 처리 : 원래는 Genre 모델을 별도로 두어 MtoN 으로 만들어야 함
# 하지만 추천기능 외에는 Genre를 딱히 쓰지 않고, 추천기능 계산할 때 처리하는 것이 훨씬 간편해서..
# 결론 : Movie 안에 TextField로 Genre를 처리함

# 그 외의 주의사항
# pk : 이 모델에서 pk는 id 값입니다.
# poster_path : 단순 파일명이어서 TextField로 해두었습니다. null 값이 아닌 것만 뽑았습니다.
# 불러올 때는 pjt10 > MovieCard.vue에서 했던 것처럼 axios를 사용하시면 됩니다.
# python manage.py loaddata movies/movies_poster2.json 하시면 됩니다. 이름은 추후에 바꾸겠습니당

class Movie(models.Model):
    # 디폴트인 id 생성하지 않음
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    overview = models.TextField()
    # poster path 임!
    poster_path = models.TextField()
    genres = models.TextField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    # 좋아요 한 영화
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')



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
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)