"""
WSGI config for djangorest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
#johan-i
import sys
#johan-f
from django.core.wsgi import get_wsgi_application

#johan-i
sys.path.append("/vagrant/djangorest/djangorest")
#johan-f
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangorest.settings")

application = get_wsgi_application()
