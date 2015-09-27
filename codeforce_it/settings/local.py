from codeforce_it.settings.base import *


INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

# The Django Debug Toolbar will only be shown to these client IPs.
INTERNAL_IPS = (
    '127.0.0.1',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'HIDE_DJANGO_SQL': False,
}


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '=#)0ha_k_v)k*uzdp1puh!o%2\=-q\=%-2y!q+3n(y^z44#ezu&v')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'codeforce_it_db'),
        'USER': os.getenv('DATABASE_USER', 'codeforce_it_db_user'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'ctnpmj78zZtSHXKV'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}