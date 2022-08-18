from django.contrib import admin
from .models import UdId
# Register your models here.

class UdIdAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'remark')
    list_editable = ('remark',)
    list_per_page = 10
    list_max_show_all = 200
    list_filter = ('content', 'remark')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(UdId, UdIdAdmin)
admin.site.site_header = "博喻传媒集群管理后台"
admin.site.site_title = "博喻传媒"
admin.site.index_title = "后台管理"