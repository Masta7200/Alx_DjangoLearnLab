from django.contrib import admin
from django.urls import path, include

from api.views import BookList  # Import include here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api.urls here
    path('books/', BookList.as_view(), name='book-list'),
]
