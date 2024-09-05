from django.urls import path
from .views import flat_views
from .views import menu_views


app_name = 'canteen'

urlpatterns = [
    path('menu-list', menu_views.menu_list, name='menu_index'),
    path('menu-add/', menu_views.menu_add, name='menu_add'),
    path('menu-edit-<int:id>/', menu_views.menu_edit, name='menu_edit'),
    path('menu-delete-<int:id>/', menu_views.menu_delete, name='menu_delete'),
    path('flat-list/', flat_views.flat_list, name='flat_index'),
    path('flat-add/', flat_views.flat_add, name='flat_add'),
    path('flat-edit-<int:id>/', flat_views.flat_edit, name='flat_edit'),
    path('flat-delete-<int:id>/', flat_views.flat_delete, name='flat_delete'),
]