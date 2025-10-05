from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """View to list all books and create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # type: ignore # Allow any user to view the list

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify
