from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
    """View to list all books and create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow any user to view the list

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
