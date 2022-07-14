from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.fields import StatusField
from model_utils import Choices


class Profile(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    STATUS = Choices('Male','Female')
    gender = StatusField(blank=True, null=True)
    image = models.ImageField(upload_to='xodim/',null=True,blank=True)
    kasb = models.CharField(max_length=100)

    def __str__(self):
        return self.username