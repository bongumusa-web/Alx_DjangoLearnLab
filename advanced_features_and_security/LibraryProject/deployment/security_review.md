# Security Review Report - HTTPS and Secure Headers

## HTTPS Configuration
- `SECURE_SSL_REDIRECT = True`: Forces all traffic to use HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces browsers to only connect via HTTPS for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS policy to subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows browser preload list enforcement.

## Secure Cookies
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` are enabled to ensure cookie transmission only over HTTPS.

## HTTP Security Headers
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking attacks.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME sniffing attacks.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser-level XSS protection.

## Deployment Configuration
- Nginx configured to redirect HTTP → HTTPS.
- SSL certificates issued via Let's Encrypt.
- Proxy headers set correctly to support Django HTTPS detection.

## Recommendations
- Monitor certificate expiry via Certbot auto-renew.
- Periodically review external scripts/styles in CSP headers.
