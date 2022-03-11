from django.urls import path
from . import views

app_name = 'parser_app'

urlpatterns = [
    path('games/', views.games_view, name='games')
]