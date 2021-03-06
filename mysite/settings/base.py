
import os
#import whitenoise

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 's&%1odi0vl9yehk47je6=-dvi&5%n$fr3x=og%+07$3@4kpd-_'


#from boto.s3.connection import S3Connection

#SECRET_KEY = S3Connection(os.environ['SECRET_KEY'])

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

##ALLOWED_HOSTS = ['qwerty9988.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'post',
]

##MIDDLEWARE = [
##    'django.middleware.security.SecurityMiddleware',
##    'whitenoise.middleware.WhiteNoiseMiddleware',
##    'django.contrib.sessions.middleware.SessionMiddleware',
##    'django.middleware.common.CommonMiddleware',
##    'django.middleware.csrf.CsrfViewMiddleware',
##    'django.contrib.auth.middleware.AuthenticationMiddleware',
##    'django.contrib.messages.middleware.MessageMiddleware',
##    'django.middleware.clickjacking.XFrameOptionsMiddleware',
##]

ROOT_URLCONF = 'mysite.urls'
MY1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [MY1 +'/templates',],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'http://dearproblems.herokuapp.com/list/'