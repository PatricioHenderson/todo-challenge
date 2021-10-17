
# Primero importamos los modelos que queremos serializar:
from applications.tareas.models import *

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers

class TareasSerializer(serializers.ModelSerializer):
    # algo =  serializers.SerializerMethodField()
    
    class Meta:
        model = Tareas
        fields = ("__all__")
        