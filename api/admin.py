# Register your models here.
from django.contrib import admin

from .models import UserData, ActivityModel

admin.site.register(UserData)
admin.site.register(ActivityModel)
