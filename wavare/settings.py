"""
Django settings for wavare project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from dotenv import load_dotenv
import os
import requests
from pathlib import Path


def is_ec2_linux():
    """Detect if we are running on an EC2 Linux Instance
    See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
    """
    if os.path.isfile("/sys/hypervisor/uuid"):
        with open("/sys/hypervisor/uuid") as f:
            uuid = f.read()
            return uuid.startswith("ec2")
    return False

def get_token():
    """Set the autorization token to live for 6 hours (maximum)"""
    headers = {
        'X-aws-ec2-metadata-token-ttl-seconds': '21600',
    }
    response = requests.put('http://169.254.169.254/latest/api/token', headers=headers)
    return response.text


def get_linux_ec2_private_ip():
    """Get the private IP Address of the machine if running on an EC2 linux server.
    See https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html"""

    if not is_ec2_linux():
        return None
    try:
        token = get_token()
        headers = {
            'X-aws-ec2-metadata-token': f"{token}",
        }
        response = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', headers=headers)
        return response.text
    except:
        return None
    finally:
        if response:
            response.close()

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Hey Brandon, the BASE_DIR is the directory containing manage.py.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["wavare.bpirrocco.dev",
                 "wavare-deploy-env.us-east-1.elasticbeanstalk.com",
                 "127.0.0.1",
                 "172.31.24.142",]
# private_ip = get_linux_ec2_private_ip()
# if private_ip:
#    ALLOWED_HOSTS.append(private_ip)


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    # Third Party Apps
    "django_apscheduler",
    "pandas",
    "unidecode",
    "django_cleanup.apps.CleanupConfig",
    "gunicorn",
    "storages",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wavare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wavare.wsgi.application'

# Caching
# Maybe move to memcached in the future
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = { 
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'wavare',
            'USER': 'wavare',
            'PASSWORD': 'testuserpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

CONN_MAX_AGE = 60


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# STORAGES = {
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage" 
#     }
# }

if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIAFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']

    AWS_S3_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media Root config
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Logging config
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

# Security and HTTP Settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False

CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [f"http://wavare-deploy-env.us-east-1.elasticbeanstalk.com",
                         "https://wavare.bpirrocco.dev",]