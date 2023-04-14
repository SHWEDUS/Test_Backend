from django.shortcuts import render
from .models import Menu


# Create your views here.

def menu(request, menu_name):
    menu_items = Menu.objects.filter(menu_name=menu_name, is_active=True)
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)
