from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.game_login, name='login'),
    path('logout', views.game_logout, name='logout'),
    path('settings', views.settings, name='settings')
]