from django.shortcuts import render
from django.http import HttpResponse
from .models import Goat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import GoatSerializer


class Goats(APIView):

    def get(self,request):
        goats = Goat.objects.all()
        serializer = GoatSerializer(goats,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = GoatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Hello, I am from views.py'}
    return render(request, 'index.html', context=my_dict)
