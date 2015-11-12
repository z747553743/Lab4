import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '.', 'site-packages'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "Lab3.settings")

import sae
from Lab3 import wsgi

application = sae.create_wsgi_app(wsgi.application)