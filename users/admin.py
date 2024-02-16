from django.contrib import admin

from django.contrib import admin
from users.models import User


class AdminUser(admin.ModelAdmin):
    list_display=["username","email"]

admin.site.register(User,AdminUser)