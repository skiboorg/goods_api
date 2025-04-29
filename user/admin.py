from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


class UserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'firstname',
        'lastname',


    )
    ordering = ('id',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'firstname',
                    'lastname',
                       'password1',
                       'password2',
                       ), }),)
    search_fields = ('id',)

    fieldsets = (
        (None, {'fields': ()}),
        ('Personal info',
         {'fields': (

         'uuid',
         'photo_url',
         'firstname',
         'lastname',
         'username',


         )}
         ),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups',)}),)


admin.site.register(User,UserAdmin)






