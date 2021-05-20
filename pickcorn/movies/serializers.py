from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed
from .models import Movie

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'