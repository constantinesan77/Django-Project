from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('lottery', views.lottery),
    path('about/', views.about),
    path('contact/', views.contact),
    path('news/', include('news.urls')),
]
