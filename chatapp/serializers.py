from rest_framework import serializers
from .models import ChatMessage
import datetime

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ( 'user', 'conversation_id')
