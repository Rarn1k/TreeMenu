from django.urls import path
from menu.views import index, draw_menu

app_name = 'menu'

urlpatterns = [
    path('', index, name='main_menu'),
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]