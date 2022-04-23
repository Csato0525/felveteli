from atexit import register
from django.contrib import admin

# Register your models here.

from APP.models import Diak

admin.site.register(Diak)