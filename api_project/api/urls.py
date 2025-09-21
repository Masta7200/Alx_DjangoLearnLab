from django.contrib import admin
from django.urls import path, include

from api.views import BookList, BookViewSet  # Import include here

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api.urls here
    path('books/', BookList.as_view(), name='book-list'),
]
