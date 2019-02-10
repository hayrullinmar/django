from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.urls import reverse


class ContentProvider(models.Model):
    title = models.CharField(max_length=127, default="ContentProviderDefault")
    description = models.TextField()
    logo = models.URLField(default="www.google.com")

    def get_absolute_url(self):
        # reverse expects the view name
        return reverse('contentprovider')

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):

    content_provider = models.ForeignKey(ContentProvider, on_delete=models.PROTECT, blank=True, null=True)

    def get_reverse_full_name(self):
        reverse_full_name = '%s %s' % (self.last_name, self.first_name)
        return reverse_full_name

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)

