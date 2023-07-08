from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'year', 'genre', 'actor']

    def validate_year(self,year ):
        if year !='1990' or year !='2000':
            raise ValidationError(detail='Error')
        return year

class Actorserializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'birthdate', 'gender']


