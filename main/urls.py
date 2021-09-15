from django.contrib import admin
from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about', views.about),
    re_path(r'^details/$', views.details),
    path('details/<str:name>/', views.details),
    re_path(r'^details/(?P<name>\D+)/$', views.details_combo),
    re_path(r'^details/(?P<name>\D+)/(?P<_id>\d+)/', views.details_combo),
    path('', include('SecretSanta.urls')),
]

admin.site.index_title = 'Администрирование Тайного Санты'
admin.site.site_title = 'Администрирование Тайного Санты'
admin.site.site_header = 'Администрирование Тайного Санты'
