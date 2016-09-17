import os

from .base import *

#Secret should come from os.environ or from a file
SECRET_KEY = 'jqvu0ytyr^*-wbkxk(3)-@9m=ht27r&j(r6(9dvw*ai0g^k)3y'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False
TEMPLATE_DEBUG_MODE = False

ALLOWED_HOSTS = ['uopy.ca']

INSTALLED_APPS = BASE_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# LOGGING
LOGGING = {
     'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
         'simple': {
             'format': '[%(asctime)s] %(levelname)s : %(message)s'
         },
         'verbose': {
             'format': '[%(asctime)s] %(levelname)s %(filename) % : %(message)s'
         },
     },
     'handlers': {
         'file': {
             'level': 'INFO',
             'class': 'logging.FileHandler',
             'formatter': 'verbose',
             'filename': BASE_DIR+'/logs/prod.log',
             'mode': 'a',
         },
     },
     'loggers': {
         'django': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
         'main.views': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
     },
 }

 #For Heroku
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
