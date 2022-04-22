from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('livecam_feed', views.livecam_feed, name='livecam_feed'),
   path('livecam_feed2', views.livecam_feed2, name='livecam_feed2'),
   path('livecam_feed3', views.livecam_feed3, name='livecam_feed3'),
]