from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import timedelta


class player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    age = models.IntegerField()
    music_type = models.CharField(max_length=30, default='NA')
    timer = models.CharField(max_length=4, default='NA')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(default=timedelta())

    def __str__(self):
        return self.first_name
