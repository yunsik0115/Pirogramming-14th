from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostL)
]