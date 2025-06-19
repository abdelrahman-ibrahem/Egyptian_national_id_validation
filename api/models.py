from django.db import models
from django.contrib.auth.models import User

class APIRequestLog(models.Model):
    """Model for tracking API requests (bonus)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.timestamp} - {self.user.username} - {self.action}"