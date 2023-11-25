from rest_framework.views import APIView
from rest_framework.response import Response
from wordcloud.models import Wordcloud
from wordcloud.serializers import WordcloudSerializer
import random



class RandomTeamsView(APIView):
    def get(self, request, format=None):
        count = request.query_params.get('count', 1)
        count = int(count)
        teams = list(Wordcloud.objects.all())
        random.shuffle(teams)
        teams = teams[:count]
        serializer = WordcloudSerializer(teams, many=True)
        return Response(serializer.data)