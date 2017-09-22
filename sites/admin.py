from django.contrib import admin

from .models import *


class ModulesInline(admin.TabularInline):
	model = Module

class SiteAdmin(admin.ModelAdmin):
    inlines = [ModulesInline, ]

admin.site.register(Site, SiteAdmin)
admin.site.register(ModuleTemplate)
admin.site.register(Module)