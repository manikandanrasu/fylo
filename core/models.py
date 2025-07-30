from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_pic = models.URLField(blank=True, null=True)
    google_id  = models.CharField(max_length=100, unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email