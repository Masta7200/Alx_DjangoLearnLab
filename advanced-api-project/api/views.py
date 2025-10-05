from tracemalloc import BaseFilter
from warnings import filters
from rest_framework import generics
from rest_framework import filters as drf_filters
from rest_framework.filters import SearchFilter
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .serializers import BookSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
class BookListView(generics.ListCreateAPIView):
    """View to list all books and create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = (drf_filters.SearchFilter, drf_filters.OrderingFilter)
    search_fields = ['title', 'author']

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'book_form.html'
    success_url = '/books/'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'book_form.html'
    success_url = '/books/'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = '/books/'

