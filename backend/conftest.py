import os
import django
from django.conf import settings

# Configure Django settings for pytest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

if not settings.configured:
    django.setup()
