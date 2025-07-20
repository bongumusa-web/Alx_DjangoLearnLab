from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author (assuming author id=1)
    author = Author.objects.get(id=1)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # List all books in a library (assuming library id=1)
    library = Library.objects.get(id=1)
    books_in_library = library.books.all()
    print(f"Books in library {library.name}: {[book.title for book in books_in_library]}")

    # Retrieve the librarian for a library (assuming library id=1)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian of {library.name}: {librarian.name}")

if __name__ == "__main__":
    run_queries()
