from rest_framework import serializers
from .models import RecNames

class RecNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecNames
        fields='__all__'