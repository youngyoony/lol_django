from rest_framework import serializers
from .models import TopPlayer

class TopPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopPlayer
        exclude = ['id', 'game_name', 'tag_line']