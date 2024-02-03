from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('singlepost/<str:pid>/', views.post, name="post")
]
