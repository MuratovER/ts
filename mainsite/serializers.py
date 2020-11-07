from rest_framework import serializers
from .models import Sphere_of_life

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sphere_of_life
        fields = ('user', 'inside_world', 'career', 'health', 'relationships')


