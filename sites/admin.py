from django.contrib import admin

from .models import *


class SiteModulesInline(admin.TabularInline):
	model = SiteModule

class SiteAdmin(admin.ModelAdmin):
    inlines = [SiteModulesInline, ]

admin.site.register(Site, SiteAdmin)
admin.site.register(Module)
admin.site.register(SiteModule)
