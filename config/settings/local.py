import os

from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

SECURE_HSTS_SECONDS = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
