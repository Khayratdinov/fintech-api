import environ
from .base import *
from .base import BASE_DIR


SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


# Check if DATABASE_SQLITE is set to True in .env
if env.bool("DATABASE_SQLITE", default=True):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # Use SQLite for development
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",  # Use PostgreSQL for production
            "NAME": env("POSTGRES_DB"),
            "USER": env("POSTGRES_USER"),
            "PASSWORD": env("POSTGRES_PASSWORD"),
            "HOST": env("POSTGRES_HOST"),
            "PORT": env("POSTGRES_PORT"),
        }
    }


SITE_NAME = env("SITE_NAME")
ADMIN_URL = env("ADMIN_URL")

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
DOMAIN = env("DOMAIN")
MAX_UPLOAD_SIZE = 1 * 1024 * 1024


CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
LOCKOUT_DURATION = timedelta(minutes=1)
LOGIN_ATTEMPTS = 3
OTP_EXPIRATION = timedelta(minutes=1)
