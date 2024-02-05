from django.db import models
from django.utils import timezone

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.body}"
    

