from .base import *


DEBUG = False

ADMINS = (
    ('Alex', 'amicharski@onetwodating.com'),
)

ALLOWED_HOSTS = ['127.0.0.1']

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['PGDATABASE'],
        'USER': config['PGUSER'],
        'PASSWORD': config['PGPASSWORD'],
        'HOST': config['PGHOST'],
        'PORT': config['PGPORT'],
        'OPTIONS': {
            'sslmode': 'require'
        },
    }
}