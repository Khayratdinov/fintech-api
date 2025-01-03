import environ
from .base import *
from .base import BASE_DIR


local_env = environ.Env(DEBUG=(bool, False))  # DEBUG uchun standart qiymat False
env_path = BASE_DIR / ".envs" / ".env.local"

local_env.read_env(env_path)

SECRET_KEY = local_env("SECRET_KEY")

DEBUG = local_env.bool("DEBUG", default=False)
ALLOWED_HOSTS = local_env.list("ALLOWED_HOSTS", default=[])
SITE_NAME = local_env("SITE_NAME")
ADMIN_URL = local_env("ADMIN_URL")

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = local_env("EMAIL_HOST")
EMAIL_PORT = local_env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = local_env("DEFAULT_FROM_EMAIL")
DOMAIN = local_env("DOMAIN")
MAX_UPLOAD_SIZE = 1 * 1024 * 1024
