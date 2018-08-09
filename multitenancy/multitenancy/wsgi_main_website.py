# wsgi_main_website.py
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings_public")

application = get_wsgi_application()
