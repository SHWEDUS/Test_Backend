from django import template
from django.urls import reverse
from menu.models import Menu

register = template.Library()


def build_menu(menu_items, current_path):
    menu_html = '<ul>'
    for item in menu_items:
        item_url = item.url if item.url else reverse(item.url_name)
        active_class = 'class="active"' if current_path == item_url else ''
        menu_html += f'<li><a href="{item_url}" {active_class}>{item.title}</a>'
        children = item.children.all()
        if children:
            menu_html += build_menu(children, current_path)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html


@register.simple_tag(takes_context=True)
def draw_menu(context, name):
    request = context['request']
    current_path = request.path
    menu_items = Menu.objects.filter(name=name).all()
    if not menu_items:
        return ''
    return build_menu(menu_items, current_path)
