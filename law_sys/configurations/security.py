"""
Security Settings
"""

import os
# import re

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]

# CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(",")

# DOMAIN_REGEX = os.environ.get("DOMAIN_REGEX")

# CORS_ALLOWED_ORIGIN_REGEXES = [
#     re.compile(DOMAIN_REGEX),
# ]

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True
