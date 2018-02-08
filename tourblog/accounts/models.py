from django.conf import settings
from django.db import models
from .validators import phone_number_validator


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20,
            validators=[phone_number_validator])

    def __str__(self):
        return '{}\'s profile'.format(self.user.username)
