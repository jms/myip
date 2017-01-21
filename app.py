#!/usr/bin/env python
""" light django app to return the client ip address """

import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'you need a secret key here, dude')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)
IPWARE_TRUSTED_PROXY_LIST = []

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from ipware.ip import get_ip

def index(request):
    """ return the client ip address """
    client_ip_address = get_ip(request)
    return HttpResponse('IP Address: {}'.format(client_ip_address))

urlpatterns = (
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

