from django.urls import path
from applications.tareas.api.hello_world_api import *


urlpatterns = [
    
    path('tareas/', GetTareasAPIView.as_view(),),
    
]
 