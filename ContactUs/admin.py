from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'create')


admin.site.register(Contact, ContactAdmin)
