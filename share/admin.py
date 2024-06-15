from django.contrib import admin

from . import models

class ShareAdmin(admin.ModelAdmin):
    list_display = ('share_id', 'symbol')

admin.site.register(models.Share, ShareAdmin)