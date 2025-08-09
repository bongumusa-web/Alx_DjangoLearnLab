from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


# Show all books (readable by anyone) + Filtering, Searching, Ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

   
    filter_backends = [
        DjangoFilterBackend,          # enables filtering
        filters.SearchFilter,         # enables search
        filters.OrderingFilter         # enables ordering
    ]
    filterset_fields = ['title', 'author', 'publication_year']  # filter by these exact fields
    search_fields = ['title', 'author']  # search in title & author
    ordering_fields = ['title', 'publication_year']  # allow ordering by these fields
    ordering = ['title']  # default ordering


# Show one book (readable by anyone)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Add a book (must be logged in)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# Update a book (must be logged in)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Delete a book (must be logged in)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
