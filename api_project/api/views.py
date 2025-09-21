from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from api.models import Book
from .serializers import BookSerializer

# Create your views here.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


