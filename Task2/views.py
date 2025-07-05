from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task2
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task2.objects.all()
    serializer_class=TaskSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['submitted']
    
