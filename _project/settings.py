import os

######################################################################

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'wb8ua=u$k3cpv*b&#63-@9d!0h)mgozggi8-(%xvxg4i1a-5&x'
DEBUG = True
ROOT_URLCONF = '_project.urls'
WSGI_APPLICATION = '_project.wsgi.application'
APPEND_SLASH = True

#--------------------------------------------------------------------

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
	}
}

# Database : https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#--------------------------------------------------------------------

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join((PROJECT_ROOT), "_static_root")
MEDIA_ROOT = os.path.join((PROJECT_ROOT), "_media_root")
STATICFILES_DIRS = ( os.path.join((PROJECT_ROOT), "static", "static"),)

# Static files : https://docs.djangoproject.com/en/1.9/howto/static-files/

#--------------------------------------------------------------------

MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#--------------------------------------------------------------------

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [ os.path.join(PROJECT_ROOT, 'static/templates/'), ],
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

#--------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
	{ 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
	{ 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
	{ 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
	{ 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Password validation : https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
# TODO : do i really need this? :o

#--------------------------------------------------------------------

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Internationalization : https://docs.djangoproject.com/en/1.9/topics/i18n/

######################################################################

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

#--------------------------------------------------------------------

INSTALLED_APPS += ['sites',]
# Main app of this project, allowing the creation and modification of minisites

#--------------------------------------------------------------------

INSTALLED_APPS += ['django_auth_network_client',]
# Authentication based on the DAN framework

LOGIN_URL = '/auth/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'

#--------------------------------------------------------------------

INSTALLED_APPS += ['bootstrap4',] # django-bootstrap4
# Utility to generate bootstrap4 forms

from django.contrib import messages
MESSAGE_TAGS = { messages.ERROR: 'danger' } # change error naming to fit bootstrap alerts

#--------------------------------------------------------------------

INSTALLED_APPS += ['rules',] # rules
# Manages row-level permissions

AUTHENTICATION_BACKENDS = (
	'rules.permissions.ObjectPermissionBackend',
	'django.contrib.auth.backends.ModelBackend',
)

#--------------------------------------------------------------------

INSTALLED_APPS += ['anymail',] # anymail

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.SendGridBackend, or...

#--------------------------------------------------------------------

######################################################################

#  Local settings : import local_settings if exist
try: from local_settings import *
except ImportError: pass