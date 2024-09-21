from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/books/')),  # Redirect root URL to books
    path('', include('relationship_app.urls')),  # Include the app's URL patterns
]



