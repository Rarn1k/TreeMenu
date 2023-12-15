from django.contrib import admin

from menu.models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    prepopulated_fields = {'url': ('name',)}
    extra = 0


@admin.register(MenuItem)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'url')
    search_fields = ('name',)
    list_filter = ('menu',)
    prepopulated_fields = {'url': ('name',)}
    empty_value_display = '-пусто-'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)
    prepopulated_fields = {'url': ('name',)}
    empty_value_display = '-пусто-'
    inlines = [MenuItemInline]
