from rest_framework import serializers

from .models import Wordcloud

class WordcloudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wordcloud
        fields = ['word']

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wordcloud
        fields = ['word','likes']