from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('makeup/', views.makeup_index, name='index'),
  path('makeup/<int:makeup_id>/', views.makeup_detail, name='detail'),
  path('makeup/create/', views.MakeupCreate.as_view(), name='makeup_create'),
  path('makeup/<int:pk>/update/', views.MakeupUpdate.as_view(), name='makeup_update'),
  path('makeup/<int:pk>/delete/', views.MakeupDelete.as_view(), name='makeup_delete'),
]

