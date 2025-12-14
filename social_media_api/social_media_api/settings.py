INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',  # For token authentication
    "DEBUG = False", "ALLOWED_HOSTS"
    # Local apps
    'accounts',"posts"
    "SECURE_BROWSER_XSS_FILTER", "X_FRAME_OPTIONS", "SECURE_SSL_REDIRECT"
]

# Django REST Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}



