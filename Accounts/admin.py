from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_admin','code','active')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Personal info',{'fields':('first_name','last_name')}),
        ('Account info',{'fields':('username','email','password','code')}),
        ('Status',{'fields':('is_active','active')}),
        ('Permission',{'fields':('is_admin',)})
    )
    add_fieldsets = (
        (None,{'fields':('first_name','last_name','email','password1','password2')}),
    )
    search_fields = ('first_name', 'last_name', 'username', 'email')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
