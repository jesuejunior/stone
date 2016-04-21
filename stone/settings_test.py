# -*- coding: utf-8 -*-
from stone.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


# LOGGING_CONFIG = True
URL = 'http://127.0.0.1:8000/'
