from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # Specify the fields to include in the form

    def clean_publication_year(self):
        # Example of custom validation for the publication year
        year = self.cleaned_data.get('publication_year')
        if year < 0:
            raise forms.ValidationError("Publication year cannot be negative.")
        return year
