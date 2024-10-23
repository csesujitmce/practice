from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=164)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
