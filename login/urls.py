from django.urls import path
from . import views
from .views import add_item, delete_item, update_item, edit_item

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('portofolio/', views.portofolio, name='portofolio'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:id>', views.blogsjasa, name='blogsjasa'),
    path('add_item', add_item, name='add_item'),
    path('delete_item/<int:id>', delete_item, name='delete_item'),
    path('update_item/<int:id>', update_item, name='update_item'),
    path('edit_item/<int:id>', edit_item, name='edit_item'),
]