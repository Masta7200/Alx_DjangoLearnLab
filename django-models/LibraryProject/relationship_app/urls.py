# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Example book listing URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Detail view for library
    path('register/', register, name='register'),  # Registration URL
    path('login/', user_login, name='login'),  # Login URL
    path('logout/', user_logout, name='logout'),  # Logout URL
]
