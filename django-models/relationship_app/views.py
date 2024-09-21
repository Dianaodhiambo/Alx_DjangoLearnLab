# relationship_app/views.py
from django.shortcuts import render
from .models import Book  # Assuming you have a Book model defined in your models.py
from django.views.generic import DetailView
from .models import Library 

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'




