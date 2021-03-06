"""
Django settings for polls project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def get_env(key, default=True):
    value = os.environ.get(key, default)
    return (value is True or value.lower() == 'true' or value == '1' or
            value.lower() == 'yes')


# Enables the ability to create a question
CAN_CREATE_QUESTION = get_env('POLLS_CAN_CREATE_QUESTION')

# Enables the ability to delete a question
CAN_DELETE_QUESTION = get_env('POLLS_CAN_DELETE_QUESTION')

# Enables the ability to vote on a question
CAN_VOTE_QUESTION = get_env('POLLS_CAN_VOTE_QUESTION')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm=%-=98*jf5hjfyjui+%5azyzr4z-$3b)q$5#1ys@6#!-#!n&e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'corsheaders',
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'polls.urls'

WSGI_APPLICATION = 'polls.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500)
}


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'pollsapi',
    }
}

CACHE_MIDDLEWARE_SECONDS = 10


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


# Logging

from django.utils.log import DEFAULT_LOGGING

LOGGING = DEFAULT_LOGGING
# Remove the debug only filter for console logging.
# We want to propergate to console and papertrail
LOGGING['handlers']['console']['filters'] = []


# CORS settings

CORS_ORIGIN_ALLOW_ALL = True
