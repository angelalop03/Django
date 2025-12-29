from django.db import models


class FavoriteArtist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite_artist")
    name = models.CharField(max_length=200)

class FavoriteTrack(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite_track")
    title = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=80, blank=True, default="")