Blog Post Management Features:

1. List all posts:
   URL: /posts/
   Accessible to all users.

2. View post detail:
   URL: /posts/<int:pk>/
   Shows full content, author, published date.

3. Create new post:
   URL: /posts/new/
   Requires login. Sets logged-in user as author.

4. Edit post:
   URL: /posts/<int:pk>/edit/
   Requires login. Only author can edit.

5. Delete post:
   URL: /posts/<int:pk>/delete/
   Requires login. Only author can delete.

Security & Permissions:
- All forms use CSRF tokens.
- Only authors can edit or delete posts.
- Passwords are stored securely using Django's hashing.

Templates:
- post_list.html, post_detail.html, post_form.html, post_confirm_delete.html
- All templates extend base.html for consistent layout.

Static Files:
- CSS stored in static/blog/css/style.css
- Can add JS in static/blog/js/ if needed

Testing:
- Verify CRUD operations.
- Ensure navigation and permissions work correctly.
- Test login, logout, registration, and profile updates.
