# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Example book listing URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Detail view for library
    path('register/', RegisterView.as_view(), name='register'),  # Registration URL
    path('login/', LoginView.as_view(), name='login'),  # Login URL
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout URL
]
