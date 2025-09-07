# relationship_app/query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

if __name__ == "__main__":
    # Example usage
    author_name = "Author Name"  # Replace with an actual author name
    print("Books by Author:", list(query_books_by_author(author_name)))

    library_name = "Library Name"  # Replace with an actual library name
    print("Books in Library:", list(list_books_in_library(library_name)))

    print("Librarian for Library:", retrieve_librarian_for_library(library_name))
