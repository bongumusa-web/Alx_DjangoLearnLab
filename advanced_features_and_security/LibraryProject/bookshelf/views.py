from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import SearchForm

def search_books(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        title = form.cleaned_data['title']
        books = Book.objects.filter(title__icontains=title)

    response = render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self'"
    return response

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
