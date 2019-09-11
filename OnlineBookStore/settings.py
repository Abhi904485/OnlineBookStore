"""
Django settings for OnlineBookStore project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oe%o0c39s^%97z5auizpi-*56iesk7^q0*@0=e(@_+9)r0w*!c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'crispy_forms',
        'widget_tweaks',
        'livereload',
        'django.contrib.staticfiles',
        'debug_toolbar',
        'accounts',
        'cart',
        'billing',
        'tags',
        'search',
        'books',
        'rest_framework',
        'django_filters',
        'contact',
        'about'
]

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'livereload.middleware.LiveReloadScript',
        'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'OnlineBookStore.urls'

INTERNAL_IPS = [
        '127.0.0.1',
]
TEMPLATES = [
        {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                        os.path.join(BASE_DIR, 'templates', 'base'),
                        os.path.join(BASE_DIR, 'books', 'templates', 'books'),
                        os.path.join(BASE_DIR, 'about', 'templates', 'about'),
                        os.path.join(BASE_DIR, 'contact', 'templates', 'contact'),
                        os.path.join(BASE_DIR, 'accounts', 'templates', 'accounts'),
                        os.path.join(BASE_DIR, 'cart', 'templates', 'cart'),

                ],
                'APP_DIRS': True,
                'OPTIONS': {
                        'context_processors': [
                                'django.template.context_processors.debug',
                                'django.template.context_processors.request',
                                'django.contrib.auth.context_processors.auth',
                                'django.contrib.messages.context_processors.messages',
                        ],
                },
        },
]

WSGI_APPLICATION = 'OnlineBookStore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "cdn", "static_root")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "cdn", "media_root")

MESSAGE_TAGS = {
        messages.SUCCESS: 'success',
        messages.ERROR: 'danger',
        messages.INFO: 'info',
        messages.WARNING: 'warning'
}

CRISPY_TEMPLATE_PACK = "bootstrap4"

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
)

LOGOUT_REDIRECT_URL = '/account/login'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/account/login'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'pstzmm@gmail.com'
EMAIL_HOST_PASSWORD = 'novell@123'
EMAIL_PORT = 587