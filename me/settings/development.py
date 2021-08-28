from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']
SECRET_KEY = 'a+nx^dwb(w+=c3l@%ysdz8ro##)#&4gb9e3jxcy7_)dvb&b+s_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'me',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mukuljindal1010@gmail.com'
EMAIL_HOST_PASSWORD = 'lngyuvbariyywcfb'
EMAIL_PORT = 587
APPLICATION_EMAIL = 'Admin<mukuljindal1010@gmail.com'
DEFAULT_FROM_EMAIL = 'Admin<mukuljindal1010@gmail.com'
