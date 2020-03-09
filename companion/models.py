from django.db import models


# Create your models here.
class Companion(models.Model):
    item_image = models.CharField(max_length=1000)

    def __str__(self):
        return self.item_image
