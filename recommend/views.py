from rest_framework.views import APIView
from rest_framework.response import Response
from recbyinput.models import RecNames
from recbyinput.serializers import RecNamesSerializer
import random



class RandomTeamsView(APIView):
    def get(self, request, format=None):
        count = request.query_params.get('count', 1)
        count = int(count)
        teams = list(RecNames.objects.all())
        random.shuffle(teams)
        teams = teams[:count]
        serializer = RecNamesSerializer(teams, many=True)
        return Response(serializer.data)