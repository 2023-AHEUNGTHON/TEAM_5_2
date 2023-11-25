# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
# from rest_framework import generics
from .models import RecNames
from .serializers import RecNamesSerializer

# Create your views here.
#앱에서의 기능 명시
#orm(object relational mapping)

class RecNamesListCreateView(generics.ListCreateAPIView):
    queryset=RecNames.objects.all()
    serializer_class=RecNamesSerializer

    #단어 list 등록
    def post(self, request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

#단어 list 모든 요소 반환
class RecNamesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecNames.objects.all()
    serializer_class = RecNamesSerializer
