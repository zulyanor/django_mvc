from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('mentee/', views.mentee, name='mentee'),
    path('mentor/', views.mentor, name='mentor'),
    path('author/', views.author, name='author'),
    path('mentee/input/', views.input_mentee),
    path('mentor/input/', views.input_mentor),
    path('blog/input/', views.input_blog),
]
