from pyverts2012 import settings
from django.core.management import setup_environ
from elements.models import Element

setup_environ(settings)

el = Element(name="test")
print el