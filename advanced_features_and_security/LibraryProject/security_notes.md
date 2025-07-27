# Security Measures Implemented

## settings.py
- `DEBUG = False` – Disables debug info in production.
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF` – Enable browser-side protections.
- `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE` – Ensure cookies are only sent over HTTPS.
- CSP middleware is used to mitigate XSS attacks.

## Templates
- All forms include `{% csrf_token %}`.

## Views
- No raw SQL used. Django ORM is used for secure queries.
- All user inputs are validated through Django forms (`forms.py`).

## Manual Testing Done
- Submitted forms without CSRF token → blocked as expected.
- Tried XSS payload in search input → rendered safely.
- Verified cookies are marked `Secure` and `HttpOnly` in browser dev tools.
