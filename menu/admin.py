from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'url', 'parent')
    list_filter = ('name',)
    search_fields = ('title', 'url')


admin.site.register(Menu, MenuAdmin)
