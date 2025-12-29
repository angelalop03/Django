from django.db import models
from users.models import User


class FavoriteArtist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite_artist")
    name = models.CharField(max_length=200)

class FavoriteTrack(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite_track")
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ["-id"]

