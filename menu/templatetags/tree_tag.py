from collections import deque

from django import template
from django.urls import resolve

from menu.models import MenuItem

register = template.Library()


def render_menu_item(items, active_item):
    results = []
    is_active = False
    for item in items:
        result = {'item': item, 'children': []}
        queue = deque([(item, result)])
        while queue and not is_active:
            current_item, current_dict = queue.popleft()
            if current_item.url == active_item:
                current_dict['children'] = []
                is_active = True
            children = current_item.children.all()
            for child in children:
                child_data = {'item': child, 'children': []}
                current_dict['children'].append(child_data)
                queue.append((child, child_data))
        results.append(result) if is_active else results.append({'item': item, 'children': []})
    return results


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(parent_id=None, menu__name=menu_name).prefetch_related('children')
    try:
        active_item = resolve(context['request'].path_info).kwargs['menu_item']
    except KeyError:
        active_item = ''
    return {'menu_items': render_menu_item(menu_items, active_item), 'active_item': active_item}
