from django.contrib import admin
from .models import Permission, Role, UserInfo, Menu

# Register your models here.

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(UserInfo)
admin.site.register(Menu)