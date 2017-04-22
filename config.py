import os

DEBUG = True

CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = os.getenv("CSRF_SECRET_KEY", "secret")

SECRET_KEY = os.getenv("SECRET_KEY", "secret")