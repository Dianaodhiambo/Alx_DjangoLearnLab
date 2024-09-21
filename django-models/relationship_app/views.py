from django.shortcuts import render
from .models import Book, Library  # Make sure to import your models

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView  # Import DetailView for class-based view

class LibraryDetailView(DetailView):
    model = Library  # The model to retrieve details from
    template_name = 'library_detail.html'  # The template to use
    context_object_name = 'library'  # Name of the context variable to use in the template




