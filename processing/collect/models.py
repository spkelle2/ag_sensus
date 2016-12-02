from __future__ import unicode_literals

from django.db import models

class Mission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    location = models.TextField() # will be a URL
    height = models.IntegerField()

    class Meta:
        ordering = ('created',)
