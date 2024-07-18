from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)