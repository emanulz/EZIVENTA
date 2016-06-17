import os
import sys


# add the hellodjango project path into the sys.path
sys.path.append('C:/Users/emanu/GITHUB/EZIVENTA/eziventa/')

# add the virtualenv site-packages path to the sys.path
sys.path.append('C:/Users/emanu/GITHUB/EZIVENTA/wezi/Lib/site-packages')

os.environ["DJANGO_SETTINGS_MODULE"] = "eziventa.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
