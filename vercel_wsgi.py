import sys
import os

from django.core.wsgi import get_wsgi_application

# Set your project name here
project_name = "Tweeter Web App"  # Replace this

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")

application = get_wsgi_application()
