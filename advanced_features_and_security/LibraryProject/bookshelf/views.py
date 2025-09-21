from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm  # Assuming you have a form for Book
from .forms import ExampleForm

def book_list(request):
    # Safe query using Django ORM
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)  # Use a Django form to validate input
        if form.is_valid():
            form.save()  # Save the book instance safely
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/form_example.html', {'form': form})

def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
