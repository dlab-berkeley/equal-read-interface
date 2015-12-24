from django.shortcuts import render, get_object_or_404
from .models import Book


def index(request):
    recommended_books = Book.objects.all()[:5]
    context = {'recommended_books': recommended_books}
    return render(request, 'index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})

def search_books(request):
    keywords = request.POST.get('drname', False).lower()
    results = {}
    results['drname'] = keywords
    results['book'] = []
    for book in Book.objects.all():
        if keywords in book.title.lower():
            results['book'].append(book)
    if len(results['book']) == 0:
        return render(request, 'search.html', {'not_found_message': 'The book you search for is not found, but here are the recommended books', 'book': Book.objects.all()})
    return render(request, 'search.html', results)
