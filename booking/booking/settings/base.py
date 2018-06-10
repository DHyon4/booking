"""
Django settings for booking project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise Exception("ImproperlyConfigured {}".format(error_msg))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%ky&g15@i)2^wn-3v95scu%*heh5ads*vgudp-px(zo@p$1^2n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',

    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',

    'macros',
    'pinax_theme_bootstrap',
    'django_extensions',
    'account',
    'sass_processor',
    'phonenumber_field',
    'social_django',
    'bootstrap3',
    'bootstrapform',
    'ordered_model',
    'rest_framework',

    'home',
    'musicians',
    'venues',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'booking.urls'

TEMPLATES_VERSIONS = ['v1', 'v2']
TEMPLATES_DESIGN_VERSION = 'v1'
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES_DIRS = [TEMPLATES_DIR] + list(map(lambda v: os.path.join(BASE_DIR, 'templates', v), TEMPLATES_VERSIONS))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.context_processors.account',
                'pinax_theme_bootstrap.context_processors.theme',

                "booking.context_processors.template_version",
                "booking.context_processors.home_url",
                "booking.context_processors.absolute_url",
                "booking.context_processors.common_words",

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'booking.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "account.auth_backends.EmailAuthenticationBackend",

    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.spotify.SpotifyOAuth2',
]

AUTH_USER_MODEL = 'home.OpusUser'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder'
]

# Cloudinary
# TODO: Eventually move to CLOUDINARY_URL
#   https://github.com/klis87/django-cloudinary-storage#installation
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'opus-dev',
    'API_KEY': '149241287193565',
    'API_SECRET': 'AhIf3zd1VNvnBBivGSxgGqHkRec'
}
# For whatever reason, you seen to need to configure both these.
CLOUDINARY = dict((k.lower(), v) for k,v in CLOUDINARY_STORAGE.items())

MEDIA_URL = '/media/'  # or any prefix you choose
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Email config
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = get_env_variable("SENDGRID_API_KEY")
SENDGRID_SANDBOX_MODE_IN_DEBUG = False

####################################
# Test CONFIG
INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '-s'
]

####################################


####################################
# REST FRAMEWORK CONFIG
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 40
}

DEFAULT_VERSION = 'v1'
ALLOWED_VERSIONS = ['v1']
# END REST FRAMEWORK CONFIG
####################################

# Account settings
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_LOGIN_REDIRECT_URL = '/m/dashboard'


# Social config
AUTHENTICATION_SETTINGS = (
  'social_core.backends.facebook.FacebookOAuth2',
  'social_core.backends.instagram.InstagramOAuth2',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
    'booking.pipeline.set_type',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/m/dashboard'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email, age_range'
}
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.10'

SOCIAL_TWITTER_CONSUMER_KEY = 'S5pewaBl5sB7rpUXnKRl8ysRZ'
SOCIAL_TWITTER_CONSUMER_SECRET = 'fKG8fOAwB3iiK72tTlyge7EBnlliHg1H5x60LUik743Om2EPUo'
SOCIAL_TWITTER_ACCESS_TOKEN = '30171536-GxwENbTPA2RF3Em1CiZ9VgZCAGpyDw4bQNWfmenuz'
SOCIAL_TWITTER_ACCESS_TOKEN_SECRET = 'oH8jw9RccbFKwQ9AgAvlnTNNxY3sjwzjxI1TTl1homk7c'
