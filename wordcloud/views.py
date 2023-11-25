from django.shortcuts import render
from rest_framework.views import status, APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Wordcloud
from .serializers import WordcloudSerializer, WordSerializer

# Create your views here.

class WordcloudView(APIView):
    def get(self, request):
        wordcloud = Wordcloud.objects.all().order_by('-likes')[:100]
        serializer = WordcloudSerializer(wordcloud, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WordView(APIView):
    def get(self, request, pk):
        word = get_object_or_404(Wordcloud, word=pk)
        serializer = WordSerializer(word)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, reqeust, pk):
        word = get_object_or_404(Wordcloud, word=pk)
        word.likes+=1
        word.save()
        serializer = WordSerializer(word)
        return Response(serializer.data, status=status.HTTP_200_OK)