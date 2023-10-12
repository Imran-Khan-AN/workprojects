from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    # Add more URL patterns here if needed
]
