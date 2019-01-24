from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pigeon',
        'USER': 'pigeon',
        'PASSWORD': '##pigeon1',  # for testing purposes only
        'HOST': 'dev03x.xenium.pl',
        'PORT': '3306',
    }
}
