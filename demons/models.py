from django.db import models


# Create your models here.
class Demon(models.Model):
    body_part = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.body_part
