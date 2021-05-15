from django.contrib import admin
from django.db.models.functions import Lower

from .models import Map, Stage

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('question', 'level', 'corresponding_map',) 
    
    def get_ordering(self, request):
        return [Lower('corresponding_map'), Lower('level')]

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'password',) 
    date_hierarchy = 'date'    
    
    def get_ordering(self, request):
        return [Lower('date')]
