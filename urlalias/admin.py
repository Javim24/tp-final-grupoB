from django.contrib import admin

# Register your models here.

from .models import URLAlias

admin.site.register(URLAlias)