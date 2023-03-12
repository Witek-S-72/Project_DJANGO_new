from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.personal_data_list, name='personal_data_list'),
    path('detail/<int:id>/', views.personal_data_detail, name='personal_data_detail'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_detail/<int:id>/', views.student_detail, name='student_detail'),


]