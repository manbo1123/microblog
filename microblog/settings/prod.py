from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {

    }
}

INSTALLED_APPS += (
    'gunicorn',
)