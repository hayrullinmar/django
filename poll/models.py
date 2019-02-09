from django.db import models
from users.models import CustomUser
from django.contrib.auth.models import User
# Create your models here.



class PollModel(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete = models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    url_logo = models.URLField()

    def __str__(self):
        return self.title