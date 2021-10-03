from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Form(models.Model):
    submit_time = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    birth_day = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, default='')
    recommend = models.CharField(max_length=100, default='')
    occupation = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)
    comment = models.CharField(max_length=4000)

    def __str__(self) -> str:
        return "{}'s form".format(self.email)