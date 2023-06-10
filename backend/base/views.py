from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Image
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ImagesSeriealizer

# Create your views here.

# class userViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

@api_view()
def images(request):
    images = Image.objects.all()
    serializer = ImagesSeriealizer(images, many = True)
    return Response(serializer.data)

@api_view()
def getImage(request, pk):
    image = Image.objects.get(id=pk)
    serializer = ImagesSeriealizer(image, many = False)
    return Response(serializer.data)