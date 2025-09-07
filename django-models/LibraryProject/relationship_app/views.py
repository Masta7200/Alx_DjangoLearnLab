from django.shortcuts import render
from django.views import View
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(View):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)  # Retrieve the library by primary key
        return render(request, 'relationship_app/library_detail.html', {'library': library})
