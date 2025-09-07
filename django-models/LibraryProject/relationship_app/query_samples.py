# relationship_app/query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Retrieve the Author object
        books = Book.objects.filter(author=author)  # Filter books by the retrieved Author
        return books
    except Author.DoesNotExist:
        return f"No author found with the name '{author_name}'."

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Retrieve the Library object
        return library.books.all()  # Return all books in the library
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'."

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Retrieve the Library object
        return library.librarian  # Return the associated Librarian
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'."
    except Librarian.DoesNotExist:
        return f"No librarian found for the library '{library_name}'."

if __name__ == "__main__":
    # Example usage
    author_name = "Author Name"  # Replace with an actual author name
    print("Books by Author:", list(query_books_by_author(author_name)))

    library_name = "Library Name"  # Replace with an actual library name
    print("Books in Library:", list(list_books_in_library(library_name)))

    print("Librarian for Library:", retrieve_librarian_for_library(library_name))
