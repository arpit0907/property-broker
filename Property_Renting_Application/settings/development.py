from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'property_renter',
        'USER':     'postgres',
        'PASSWORD': 'psql',
        'HOST':     'localhost',
        'PORT':     5432,
    }
}


DEFAULT_FROM_EMAIL = 'property@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587


# local settings
try:
    from .local import *
except ImportError:
    pass