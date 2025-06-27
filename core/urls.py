from django.urls import path
from .views import MelhorCotacaoView

urlpatterns = [
    path("melhor-cotacao/", MelhorCotacaoView.as_view(), name="melhor-cotacao"),
]