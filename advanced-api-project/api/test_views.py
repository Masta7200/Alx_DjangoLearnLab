from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a book instance for testing
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2023
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        """Test creating a new book"""
        response = self.client.post(reverse('book-list'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # One existing + one new
        self.assertEqual(Book.objects.last().title, 'Test Book')

    def test_retrieve_book(self):
        """Test retrieving a book"""
        response = self.client.get(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """Test updating a book"""
        update_data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2024
        }
        response = self.client.put(reverse('book-detail', args=[self.book.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Book should be deleted

    def test_filter_books(self):
        """Test filtering books by title"""
        Book.objects.create(title='Another Book', author='Another Author', publication_year=2022)
        response = self.client.get(reverse('book-list') + '?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book should match

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(reverse('book-list') + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should find the Test Book

    def test_order_books(self):
        """Test ordering books by publication year"""
        Book.objects.create(title='Old Book', author='Old Author', publication_year=2020)
        response = self.client.get(reverse('book-list') + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Old Book')  # Old Book should come first

    def test_permissions(self):
        """Test permissions for creating a book"""
        self.client.logout()  # Log out the user
        response = self.client.post(reverse('book-list'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Should be forbidden
