from django.contrib import admin
from .models import  MyUser




@admin.register(MyUser)
class AdminMyuser(admin.ModelAdmin):
    list_display =('username', 'last_name', 'first_name', 'is_active', 'is_staff')

# admin.site.register(MyUser) 