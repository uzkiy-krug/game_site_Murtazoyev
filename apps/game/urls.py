from django.urls import path
from .views import GamesView

app_name = 'game'

urlpatterns = [
    path('', GamesView.as_view(), name="games")
]
