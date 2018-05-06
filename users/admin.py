from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UsersAdmin(UserAdmin):

    fieldsets = (
        ('User',{'fields': ('email','password')}),
        ('Info Personal', {'fields':('first_name','last_name',
                                        'address','phone','avatar')})
    )

    add_fieldsets = (
        ('User',{'fields': ('email','password')}),
        ('Info Personal', {'fields':('first_name','last_name',
                                        'address','phone','avatar')})
    )
    
    list_display=['first_name','email']
    ordering = ['email']

admin.site.register(User,UsersAdmin)




