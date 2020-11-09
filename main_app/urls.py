from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('makeup/', views.makeup_index, name='index'),
  path('makeup/<int:makeup_id>/', views.makeup_detail, name='detail'),
]