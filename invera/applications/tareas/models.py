from django.db import models

# Create your models here.

class Tareas(models.Model):
    id = models.BigAutoField(
        db_column='ID',
        primary_key=True)

    nombre_tarea = models.CharField(
        verbose_name='Tarea',
        max_length=20,
        blank=True)

    estado_tarea = models.BooleanField(
        verbose_name='Tarea completada',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha creacion',
        )

    class Meta:
        db_table = 'tarea'

    def __str__(self):
        return f'{self.nombre_tarea}'