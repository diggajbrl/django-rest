from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class StudentListApiView (generics.ListCreateAPIView) :
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView (generics.RetrieveUpdateDestroyAPIView) :
    queryset = Student.objects.all()
    serializer_class = StudentSerializer