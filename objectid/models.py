from django.db import models
from users.models import CustomUser
from django.contrib.auth.models import User

# Create your models here.


class Artwork(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=128, null = True, blank=True)

    def __str__(self):
        return "ARTWORK {}".format(self.id)
