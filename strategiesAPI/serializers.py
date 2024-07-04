from .models import strategiesList
from rest_framework import serializers

class strategyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = strategiesList
        fields = ['id', 'name', 'script']
