from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

#Vercel Envionment Settings
'''
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

#Local Envionment Settings
'''
SECRET_KEY = ("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "polls",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sfeed_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sfeed_project.wsgi.application"


# Database



#LOCAL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sfeed_project',
        'USER': 'sfeed_admin',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'verceldb',
        'USER': 'default',
        'PASSWORD': 'SudsAaFN4c8o',
        'HOST': 'ep-shy-cell-a4b05nt6-pooler.us-east-1.aws.neon.tech',
        'PORT': '5432',
    }
}


POSTGRES_USER = os.getenv('POSTGRES_USER', 'default')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'SudsAaFN4c8o')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'ep-shy-cell-a4b05nt6-pooler.us-east-1.aws.neon.tech')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE', 'verceldb')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DATABASE,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': '5432',
    }
}
'''

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

#For Local # Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_DIRS = [BASE_DIR / 'polls/static']

# For Vercel # Static files (CSS, JavaScript, Images)
'''
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
'''
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
