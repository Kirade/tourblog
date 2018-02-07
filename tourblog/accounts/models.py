from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)


    # phone_number에 대한 validator 추가해야함

