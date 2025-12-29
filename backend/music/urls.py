from django.urls import path
from .views import FavoriteArtistAPIView, FavoriteTrackAPIView

urlpatterns = [
    path("users/<int:user_id>/artist/", FavoriteArtistAPIView.as_view()),
    path("users/<int:user_id>/track/", FavoriteTrackAPIView.as_view()),
]
