from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.notes_list, name='notes_list'),
    path('detail/<int:id>', views.notes_detail, name='notes_detail'),
    path('category/list/', views.category_list, name='category_list'),
    path('category/detail/<int:id>', views.category_detail, name='category_detail'),




    ]
