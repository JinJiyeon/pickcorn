from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('<int:pk>/recommend/', views.recommend, name='recommend'),
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail, name='detail'),
]
