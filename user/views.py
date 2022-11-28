from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"success":"User registration successfull","status":status.HTTP_200_OK})
    return Response({"error":serializer.errors,"status":status.HTTP_400_BAD_REQUEST})