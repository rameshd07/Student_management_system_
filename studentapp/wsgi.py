"""
WSGI config for student_management_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os
from django.core.wsgi import get_wsgi_application

# 👇 Replace 'student_management_system' with the exact name of your project folder
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'student_management_system.settings')

application = get_wsgi_application()
