# LibraryProject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/books/')),  # Redirect the root URL to the books list
    path('', include('relationship_app.urls')),  # Include the app's URL patterns
]





