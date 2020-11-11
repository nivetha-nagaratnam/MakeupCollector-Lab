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
  path('makeup/<int:makeup_id>/add_review/', views.add_review, name='add_review'),
  path('makeup/<int:makeup_id>/add_photo/', views.add_photo, name='add_photo'),
  path('makeup/<int:makeup_id>/assoc_dupe/<int:dupe_id>/', views.assoc_dupe, name='assoc_dupe'),
  path('makeup/<int:makeup_id>/unassoc_dupe/<int:dupe_id>/', views.unassoc_dupe, name='unassoc_dupe'),
  path('dupes/', views.DupeList.as_view(), name='dupes_index'),
  path('dupes/<int:pk>/', views.DupeDetail.as_view(), name='dupes_detail'),
  path('dupes/create/', views.DupeCreate.as_view(), name='dupes_create'),
  path('dupes/<int:pk>/update/', views.DupeUpdate.as_view(), name='dupes_update'),
  path('dupes/<int:pk>/delete/', views.DupeDelete.as_view(), name='dupes_delete'),
]

