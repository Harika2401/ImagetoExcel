from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *
admin.site.register(Customer)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


