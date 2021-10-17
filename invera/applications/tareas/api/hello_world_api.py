# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from applications.tareas.api.serializers import *
from applications.tareas.models import *
# (GET) Listar todos los elementos en la entidad:
from rest_framework.generics import ListAPIView



class GetTareasAPIView(ListAPIView):
    __doc__ = f'''
    `[METODO GET]`
    Esta vista de API nos devuelve una lista de todos los comics presentes en la base de datos.
    '''
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    permission_classes = []

