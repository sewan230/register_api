from rest_framework import serializers
from .models import Task2
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task2
        fields='__all__'