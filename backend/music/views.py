from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from .models import FavoriteArtist, FavoriteTrack
from .serializer import FavoriteArtistSerializer, FavoriteTrackSerializer


class FavoriteArtistAPIView(APIView):
    """
    Artista favorito por usuario:
    GET/POST/PUT/DELETE /api/users/{user_id}/artist/
    """

    def get(self, request, user_id: int):
        try:
            fav = FavoriteArtist.objects.get(user_id=user_id)
            return Response(FavoriteArtistSerializer(fav).data, status=status.HTTP_200_OK)
        except FavoriteArtist.DoesNotExist:
            return Response({"detail": "No favorite artist for this user."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id: int):
        # valida que exista el usuario
        if not User.objects.filter(id=user_id).exists():
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # evita duplicado (OneToOne)
        if FavoriteArtist.objects.filter(user_id=user_id).exists():
            return Response({"detail": "Favorite artist already exists. Use PUT to update."},
                            status=status.HTTP_409_CONFLICT)

        data = request.data.copy()
        data["user"] = user_id

        serializer = FavoriteArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id: int):
        if not User.objects.filter(id=user_id).exists():
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        fav, created = FavoriteArtist.objects.get_or_create(user_id=user_id, defaults={"name": ""})

        data = request.data.copy()
        data["user"] = user_id

        serializer = FavoriteArtistSerializer(fav, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id: int):
        deleted, _ = FavoriteArtist.objects.filter(user_id=user_id).delete()
        if deleted == 0:
            return Response({"detail": "No favorite artist to delete."}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class FavoriteTrackAPIView(APIView):
    """
    Canción favorita por usuario:
    GET/POST/PUT/DELETE /api/users/{user_id}/track/
    """

    def get(self, request, user_id: int):
        try:
            fav = FavoriteTrack.objects.get(user_id=user_id)
            return Response(FavoriteTrackSerializer(fav).data, status=status.HTTP_200_OK)
        except FavoriteTrack.DoesNotExist:
            return Response({"detail": "No favorite track for this user."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id: int):
        if not User.objects.filter(id=user_id).exists():
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if FavoriteTrack.objects.filter(user_id=user_id).exists():
            return Response({"detail": "Favorite track already exists. Use PUT to update."},
                            status=status.HTTP_409_CONFLICT)

        data = request.data.copy()
        data["user"] = user_id

        serializer = FavoriteTrackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id: int):
        if not User.objects.filter(id=user_id).exists():
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        fav, created = FavoriteTrack.objects.get_or_create(user_id=user_id, defaults={"title": ""})

        data = request.data.copy()
        data["user"] = user_id

        serializer = FavoriteTrackSerializer(fav, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id: int):
        deleted, _ = FavoriteTrack.objects.filter(user_id=user_id).delete()
        if deleted == 0:
            return Response({"detail": "No favorite track to delete."}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
