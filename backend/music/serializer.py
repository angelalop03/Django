from rest_framework import serializers
from .models import FavoriteArtist, FavoriteTrack


class FavoriteArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteArtist
        fields = ["id", "user", "name"]
        read_only_fields = ["id"]


class FavoriteTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTrack
        fields = ["id", "user", "title"]
        read_only_fields = ["id"]
