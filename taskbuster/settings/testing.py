# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_rest_tools_tests', # get_env_variable('DATABASE_NAME'),
        'USER': 'postgres', # get_env_variable('DATABASE_USER'),
        'PASSWORD': 'postgres', # get_env_variable('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
    )
