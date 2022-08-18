from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'telephone', 'email',
     'username', 'date_joined', 'is_active', 'is_staff')
    list_per_page = 5
    list_filter = ('username', 'email')
    readonly_fields = ('date_joined',)
    fieldsets = (
        (None, {
            "fields": ('telephone', 'password', 'email', 'username', 'avatar', 'date_joined', 'is_active', 'is_staff'),
        }),
    )

# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.site_header = "博喻集群管理后台"
# admin.site.site_title = "博喻集群"
# admin.site.index_title = "后台管理"