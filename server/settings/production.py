from base import *
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get("PRODUCTION_KEY ")
ALLOWED_HOSTS = ['*']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql', # Corrected typo here
#         'NAME': os.environ.get("NAME"),      # Database name
#         'USER': os.environ.get("USER"),      # Database user
#         'PASSWORD': os.environ.get("PASSWORD"),  # Database password
#         'HOST': os.environ.get("HOST"),      # Database host
#         'PORT': os.environ.get("PORT"),      # Database port (leave empty for default)
#     }
# }

ALLOWED_HOSTS = []

CORS_ALLOW_ALL_ORIGINS = True 

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500"

]