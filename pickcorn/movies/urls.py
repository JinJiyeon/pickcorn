from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 전체영화정보 제공 => index
    path('', views.index, name='index'),
    # 단일 영화정보 제공 => detail
    path('<int:movie_pk>/', views.detail, name='detail'),
    # # 리뷰 생성, 리뷰 정보 반환, 리뷰 수정, 리뷰 삭제 (CRUD)
    # path('<int:movie_pk>/articles/', views.movie_articles),
    # path('articles/<int:pk>/', views.article_detail),
    # # 댓글 생성, 반환
    # path('comments/', views.comments),
    # path('comments/<int:pk>/', views.comment_detail),
    # path('articles/<int:article_pk>/comments/', views.article_comments),
    path('<int:movie_pk>/article/', views.article_create, name='article_create'),
    path('<int:article_pk>/', views.article_detail, name='detail'),
    path('<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/like/', views.like, name='like'),
]
