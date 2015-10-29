from django.shortcuts import render, get_object_or_404
from .models import Book


def index(request):
    book_list = Book.objects.all()
    return render(request, 'index.html', {'book_list': book_list})


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})
