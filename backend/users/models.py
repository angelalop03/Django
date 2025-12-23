from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    @classmethod
    def create_user(cls):
        cls.objects.create(
            username="testuser",
            email="testuser@example.com",
            age=25)
        
        cls.objects.create(
            username="Angela",
            email="angela@example.com",
            age=22)
