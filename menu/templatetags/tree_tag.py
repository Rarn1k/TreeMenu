from django import template
from menu.models import MenuItem

register = template.Library()


def render_menu_item(item):
    children = item.children.all()
    return {'item': item, 'children': [render_menu_item(child) for child in children]}


@register.inclusion_tag('menu/menu_template.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent_id=None, menu__name=menu_name).prefetch_related('children')
    print(menu_items)
    return {'menu_items': [render_menu_item(item) for item in menu_items]}
