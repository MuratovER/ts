from rest_framework import serializers
from .models import Sphere_of_life

class TodoListSerializer(serializers.ModelSerializer): # В будущем заготовка для "ежедневника"
    class Meta:
        model = Sphere_of_life
        fields = ('user', 'inside_world', 'career', 'health', 'relationships')


