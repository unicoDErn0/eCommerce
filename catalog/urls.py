from django.urls import path
from django.contrib import admin
from . import views

# urlpatterns = [
#      path('login/', views.login_view, name='login_view'),
# ]
# yourapp/urls.py

app_name = 'catalog'  # Add the namespace here

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),  
    path('login/register/', views.register, name='register'),

]
