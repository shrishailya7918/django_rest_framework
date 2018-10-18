from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CelebrityTable
from .serializers import CelebritySerializer


def homeView(request):
    return render(request, 'Celebrity/Celebrity.html')

class RestOperations(APIView):

    def get(self, request):
        celebrities = CelebrityTable.objects.all()
        celebritiesInfo = CelebritySerializer(celebrities, many = True)
        return Response(celebritiesInfo.data, status=status.HTTP_200_OK)

    def post(self, request):
        celebrityInfo = CelebritySerializer(data=request.data)
        if celebrityInfo.is_valid():
            celebrityInfo.save()
            return Response("Successfully inserted data of "+request.data['name'], status=status.HTTP_200_OK)
        return Response(celebrityInfo.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        celebrityData = get_object_or_404(CelebrityTable, name=request.data['name'])
        celebrityInfo = CelebritySerializer(celebrityData, data=request.data)
        if celebrityInfo.is_valid():
            celebrityInfo.save()
            return Response("Modification successfully done of "+request.data['name'], status=status.HTTP_200_OK)
        return Response(celebrityInfo.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        CelebrityData = get_object_or_404(CelebrityTable, name = request.data['name'])
        CelebrityData.delete()
        celebrities = CelebrityTable.objects.all()
        CelebrityInfo = CelebritySerializer(celebrities, many=True)
        return Response("Successfully deleted data of +"+request.data['name']+" now recorded data is "+CelebrityInfo.data, status=status.HTTP_200_OK)