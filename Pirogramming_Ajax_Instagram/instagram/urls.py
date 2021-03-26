from django.urls import path
from instagram import views

app_name = 'instagram'

urlpatterns = [
    path('', views.PhotoLV.as_view(), name='photo_list'),
    path('<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
]