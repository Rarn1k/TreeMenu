from django.shortcuts import render

from menu.models import Menu


def index(request):
    return render(request, 'menu/index.html', {'menus': Menu.objects.all()})


def draw_menu(request, menu_name, menu_item=None):
    return render(request, 'menu/index.html', {'menu_name': menu_name, 'menu_item': menu_item})
