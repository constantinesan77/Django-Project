from django.urls import path, include
from django.views.generic import ListView, DetailView
from news.models import Post

urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all(), template_name="news/posts_test.html")),
    path('<int:pk>/', DetailView.as_view(model=Post, template_name="news/post_test.html")),
]
