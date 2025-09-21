from django.contrib import admin
from django.urls import path, include  # Import include here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api.urls here
]
