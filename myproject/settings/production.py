from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-web-ipaddress', 'www.website.com']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'our-db-name',
        'USER': 'our-dbuser-name',
        'PASSW0RD': 'our-db-password',
        'HOST': 'localhost',
        'PORT': ''
    }
}


STRIPE_PUBLIC_KEY = 'our-public-key'
STRIPE_PRIVATE_KEY = 'our-private-key'