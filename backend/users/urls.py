from django.urls import path
from .views import UserViewSet, UserDetailView

urlpatterns = [
    path('users/', UserViewSet.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]