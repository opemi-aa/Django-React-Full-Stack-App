from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ActionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action_time = models.DateTimeField(auto_now_add=True)
    action_description = models.CharField(max_length=255)
    note_affected = models.ForeignKey('Note', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.action_description} at {self.action_time}'
