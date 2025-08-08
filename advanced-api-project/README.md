# Advanced API Project - Book Views

## Generic Views Overview

The following DRF generic views are implemented for the `Book` model:

### Endpoints

- `GET /books/`: List all books (public)
- `GET /books/<pk>/`: Retrieve single book (public)
- `POST /books/create/`: Create new book (authenticated users)
- `PUT /books/<pk>/update/`: Update book (authenticated users)
- `DELETE /books/<pk>/delete/`: Delete book (authenticated users)

## Permissions

- `AllowAny` for read operations (List & Detail)
- `IsAuthenticated` for write operations (Create, Update, Delete)

## Custom Behavior

- `perform_create` is used in `BookCreateView` to customize creation logic.
- Permissions ensure proper access control based on authentication.

## Testing

Use tools like Postman or curl to test endpoints. Include authorization headers for create/update/delete operations.
