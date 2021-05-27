from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 전체영화정보 제공 => index
    path('', views.index, name='index'),
    # path('tst/', views.tst, name='tst'),
    # 단일 영화정보 제공 => detail
    path('<int:movie_pk>/', views.detail, name='detail'),

    path('<int:movie_pk>/article/', views.article_create, name='article_create'),
    path('article/<int:article_pk>/', views.article_detail, name='article_detail'),
    path('article/<int:article_pk>/update/', views.article_update, name='article_update'),
    path('article/<int:article_pk>/delete/', views.article_delete, name='article_delete'),

    path('article/<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    path('comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('<int:movie_pk>/rate_good/', views.rate_good, name='rate_good'),
    path('<int:movie_pk>/rate_bad/', views.rate_bad, name='rate_bad'),

    path('searchpage/', views.searchpage, name='searchpage'),
    path('homepage/', views.homepage, name='homepage'),
]
