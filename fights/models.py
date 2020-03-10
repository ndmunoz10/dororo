from django.db import models


# Create your models here.
class Fight(models.Model):
    winner_name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    demon_image = models.CharField(max_length=1000)

    def __str__(self):
        return self.winner_name
