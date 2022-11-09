from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Pool , Asset

# Register your models here.
admin.site.register(Pool)
admin.site.register(Asset)
