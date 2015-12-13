"""
Django settings for ARPixelSite project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# -*- coding: utf-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

gettext = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@-$h5gh5%s$70hd=ii55it!+4@a*u8b(c8aqumqkx@*m8%v89l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'cms',  # django CMS itself
	# 'treebeard',  # utilities for implementing a tree
	# 'menus',  # helper for model independent hierarchical website navigation
	# #'south',  # Only needed for Django < 1.7
	# 'sekizai',  # for javascript and css management
	# 'djangocms_file',
	# 'djangocms_flash',
	# 'djangocms_googlemap',
	# 'djangocms_inherit',
	# 'djangocms_picture',
	# 'djangocms_teaser',
	# 'djangocms_video',
	# 'djangocms_link',
	# 'djangocms_snippet',
    'rest_framework',
    'clientupload',
    'authenticateclients',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'cms.middleware.user.CurrentUserMiddleware',
    #'cms.middleware.page.CurrentPageMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',
    #'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'ARPixelSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
			    'django.core.context_processors.request',
			    'django.core.context_processors.media',
			    'django.core.context_processors.static',
			    #'sekizai.context_processors.sekizai',
			    #'cms.context_processors.cms_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'ARPixelSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ARPixelDB',
        'USER': 'djangouser',
        'PASSWORD': 'djangouser',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.authentication.SessionAuthentication',
#    ),
#    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
#    'PAGE_SIZE': 10
#}

"""
TEMPLATE_DIRS = (
    # The docs say it should be absolute path: BASE_DIR is precisely one.
    # Life is wonderful!
    os.path.join(BASE_DIR, "templates"),
)
"""
"""
CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)
"""
"""
LANGUAGES = [
    ('en', 'English'),
]
"""

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

#CMS_PAGE_MEDIA_PATH = os.path.join(MEDIA_ROOT, "cms_page_media")

#AUTH_USER_MODEL = 'authenticateclients.UploaderClient'