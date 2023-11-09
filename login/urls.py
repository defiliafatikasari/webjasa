from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('blogs/', views.blogs, name='blogs'),
]