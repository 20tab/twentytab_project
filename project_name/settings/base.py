"""
Django settings for {{project_name}} project.

Generated by 'django-admin startproject' using Django {{django_version}}.

For more information on this file, see
https://docs.djangoproject.com/en/{{docs_version}}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{docs_version}}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secretkey-to-change-in-secret-py'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{project_name}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = '{{project_name}}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/{{docs_version}}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{docs_version}}/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = None  # NOTE: to use only with collectstatic workflow

STATICFILES_DIRS = (os.path.abspath(os.path.join(BASE_DIR, 'static')),)

# Stored files
# https://docs.djangoproject.com/en/{{docs_version}}/topics/files/

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))


# Sites

DEFAULT_NAME = '{{project_name}}'

BASE_HOST_URL = '{{project_name}}.com'

BASE_URL = f'www.{BASE_HOST_URL}'

BASE_DOMAIN_URL = f'http://{BASE_URL}'


# Email Settings
# https://docs.djangoproject.com/en/{{docs_version}}/topics/email/

SERVER_EMAIL = f'info@{BASE_HOST_URL}'

DEFAULT_FROM_EMAIL = f'{DEFAULT_NAME} <{SERVER_EMAIL}>'

EMAIL_SUBJECT_PREFIX = f'[{DEFAULT_NAME}] '

EMAIL_USE_LOCALTIME = True

ERROR_EMAIL = f'errors@{BASE_HOST_URL}'

EMAIL_SIGNATURE = f'\n-- \n{DEFAULT_FROM_EMAIL}'

MANAGERS = ((DEFAULT_NAME, ERROR_EMAIL),)

ADMINS = MANAGERS


# Translation
# https://docs.djangoproject.com/en/{{docs_version}}/topics/i18n/translation/

# LANGUAGES = (
#     ('en', 'English'),
#     ('it', 'Italiano'),
# )

# LOCALE_PATHS = (os.path.abspath(os.path.join(BASE_DIR, 'locale')),)


# Authentication
# https://docs.djangoproject.com/en/{{docs_version}}/topics/auth/customizing/

# AUTH_USER_MODEL = 'users.User'

# LOGIN_URL = 'login'

# LOGOUT_URL = 'logout'

# LOGIN_ERROR_URL = 'home'

# LOGIN_REDIRECT_URL = 'home'

# LOGOUT_REDIRECT_URL = 'home'
