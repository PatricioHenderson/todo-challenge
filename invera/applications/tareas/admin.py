from django.contrib import admin

# Locals
from applications.tareas.models import *

# Register your models here.

@admin.register(Tareas)
class tareas_listAdmin(admin.ModelAdmin):
    search_fields = ['nombre_tarea' , 'created_at']
    list_display = ['nombre_tarea' , 'estado_tarea' , 'created_at' ]



