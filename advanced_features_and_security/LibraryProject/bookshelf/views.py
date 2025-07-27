from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import SearchForm # Include ExampleForm
from .forms import ExampleForm

# Secure Search View
def search_books(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        title = form.cleaned_data['title']
        books = Book.objects.filter(title__icontains=title)

    response = render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self'"
    return response

# Permissions-protected Book List
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# New View to Handle ExampleForm Securely
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process cleaned data securely
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Simulate save / action here
            return render(request, 'bookshelf/form_example.html', {'form': ExampleForm(), 'success': True})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
