from django.contrib import admin
from django.urls import path

from .views import (main_map_view,
					map_selection_view,
					map_creation_view)

app_name = 'map'

urlpatterns = [
	path('', main_map_view, name='main_map'),
    path('select/', map_selection_view, name='select'),
    path('create/', map_creation_view, name='create')
]