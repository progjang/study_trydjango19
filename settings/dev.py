from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "settings", "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")