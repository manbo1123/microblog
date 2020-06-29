from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'microblog',
      'USER': 'microblog',
      'PASSWORD': 'microblog',
    }
}

INSTALLED_APPS += (
    'gunicorn',
)
