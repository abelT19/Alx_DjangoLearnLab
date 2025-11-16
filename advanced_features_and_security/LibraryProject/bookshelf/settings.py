# SECURITY SETTINGS FOR HTTPS

# Redirect all HTTP requests to HTTPS
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # ✅ Ensures all HTTP requests are redirected to HTTPS

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Clickjacking protection
X_FRAME_OPTIONS = "DENY"

# Prevent content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True  # Redirects all non-HTTPS requests to HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS policy to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow the site to be included in browsers' HSTS preload list

# Secure cookies
SESSION_COOKIE_SECURE = True  # Only transmit session cookies over HTTPS
CSRF_COOKIE_SECURE = True     # Only transmit CSRF cookies over HTTPS

# Clickjacking protection
X_FRAME_OPTIONS = "DENY"  # Prevent the site from being embedded in frames

# Content-type sniffing protection
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from MIME-sniffing

# XSS protection in browsers
SECURE_BROWSER_XSS_FILTER = True  # Enable the browser's XSS filter

# Note: Ensure DEBUG is False in production
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']  # Replace with your production domain

