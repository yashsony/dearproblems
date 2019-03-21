from .base import *

SECRET_KEY = '_9qvh)@90*2l1^^-o3cgpz*ezkx9w&@+x#*4zf_jkn63po)b8e'

DEBUG = True

ALLOWED_HOSTS = []


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'
#PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
MY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIC_ROOT  =   os.path.join(MY, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(MY, 'static'),

)