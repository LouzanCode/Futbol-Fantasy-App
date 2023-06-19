from django.urls import path

from .views import AdminViews, AppViews

app_name = 'home'

urlpatterns = [
    path('adminr/', AdminViews.actualitzar_dades, name='registro'),
    path('', AppViews.home, name='home'),
    path('player/<slug:slug>/', AppViews.player_detail, name='player_detail'),
    path('players/', AppViews.players, name='players'),
    
]