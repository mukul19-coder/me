from .base import *
import os
from dotenv import load_dotenv
import random

DEBUG = False

dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'.env')
load_dotenv(dotenv_path)

ALLOWED_HOSTS = ['65.0.73.228']
SECRET_KEY = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
APPLICATION_EMAIL = 'Admin<mukuljindal1010@gmail.com'
DEFAULT_FROM_EMAIL = 'Admin<mukuljindal1010@gmail.com'


STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')