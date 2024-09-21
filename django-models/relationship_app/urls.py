# relationship_app/urls.py
from django.urls import path
from .views import list_books
from .views import list_books, LibraryDetailView

# Edit relationship_app/urls.py to include URL patterns that route to the newly created views.
urlpatterns = [
    path('books/', list_books, name='list_books'),  # Link to the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Link to the class-based view
]


