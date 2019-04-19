from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ('location', 'time', 'capacity')
    fieldsets = [
        (None,               {'fields': ['location', 'time', 'capacity', 'students']}),
    ]
    filter_horizontal = ('students',)


admin.site.register(User, UserAdmin)
admin.site.register(Site, SiteAdmin)
