from .common import *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'czph4#9hjg2izx6tvr*5*xibj68w-s9hsc4f3fj(ah%t$4^2z!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + (
    'rest_framework.renderers.BrowsableAPIRenderer',
)

ALLOWED_HOSTS = ["localhost"]
