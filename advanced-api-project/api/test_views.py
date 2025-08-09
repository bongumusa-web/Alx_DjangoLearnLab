from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book


class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="tester", password="pass1234")

        # Create some book data
        self.book1 = Book.objects.create(
            title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937
        )
        self.book2 = Book.objects.create(
            title="The Lord of the Rings", author="J.R.R. Tolkien", publication_year=1954
        )
        self.book3 = Book.objects.create(
            title="Harry Potter", author="J.K. Rowling", publication_year=1997
        )

        self.list_url = reverse("book-list")  # ensure your URL name matches
        self.create_url = reverse("book-create")  # ensure your URL name matches

    def test_list_books(self):
        """Anyone can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book(self):
        """Anyone can retrieve a single book"""
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Hobbit")

    def test_create_book_requires_authentication(self):
        """POST should fail for unauthenticated"""
        data = {"title": "New Book", "author": "Anon", "publication_year": 2020}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """POST works when logged in"""
        self.client.login(username="tester", password="pass1234")
        data = {"title": "New Book", "author": "Tester", "publication_year": 2024}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book(self):
        """PUT requires authentication"""
        url = reverse("book-update", args=[self.book1.id])
        self.client.login(username="tester", password="pass1234")
        data = {"title": "The Hobbit Updated", "author": "J.R.R. Tolkien", "publication_year": 1937}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "The Hobbit Updated")

    def test_delete_book(self):
        """DELETE requires authentication"""
        url = reverse("book-delete", args=[self.book1.id])
        self.client.login(username="tester", password="pass1234")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_title(self):
        """Filter by title returns correct results"""
        response = self.client.get(f"{self.list_url}?title=The Hobbit")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_search_books(self):
        """Search in title or author"""
        response = self.client.get(f"{self.list_url}?search=tolkien")
        titles = [book["title"] for book in response.data]
        self.assertIn("The Hobbit", titles)
        self.assertIn("The Lord of the Rings", titles)
        self.assertNotIn("Harry Potter", titles)

    def test_order_books_by_year_desc(self):
        """Ordering results by publication_year descending"""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
