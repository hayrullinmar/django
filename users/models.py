from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class ContentProvider(models.Model):
    title = models.CharField(max_length=127, default="ContentProviderDefault")
    description = models.TextField()
    logo = models.URLField()


class CustomUser(AbstractUser):

    content_provider = models.ForeignKey(ContentProvider, on_delete=models.PROTECT, blank=True, null=True)
    def get_reverse_full_name(self):
        reverse_full_name = '%s %s' % (self.last_name, self.first_name)
        return reverse_full_name

    def save(self, *args, **kwargs):
        print("Custom user model is saved")
        print("args are {}".format(args))
        print("kwargs are {}".format(kwargs))

        super(CustomUser, self).save(*args, **kwargs)
