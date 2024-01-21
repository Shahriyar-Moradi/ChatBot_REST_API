# chatbot_app/models.py
from django.db import models

class ChatMessage(models.Model):
    user_text = models.CharField(max_length=255)
    bot = models.CharField(max_length=255)
    conversation_id = models.CharField(max_length=100)
    history = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        # Provide a default value for the bot field if not provided
        if not self.bot:
            self.bot = "DefaultBot"
        super().save(*args, **kwargs)