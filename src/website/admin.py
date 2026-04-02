from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import record

# Register your models here.
admin.site.register(record)

