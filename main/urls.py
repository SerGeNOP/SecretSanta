from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    re_path(r'^details/$', views.details),
    path('details/<str:name>/', views.details),
    re_path(r'^details/(?P<name>\D+)/$', views.details_combo),
    re_path(r'^details/(?P<name>\D+)/(?P<_id>\d+)/', views.details_combo),
]
