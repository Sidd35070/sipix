from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Image

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ImagesSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'