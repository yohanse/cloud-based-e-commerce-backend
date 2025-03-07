from .settings import * # Import all settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite in memory
        'NAME': ':memory:',
    }
}