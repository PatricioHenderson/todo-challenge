# Getting Started
En caso de utilizar docker:

Descargar la imagen desde docker con el comando docker pull docker.io/patriciohenderson/invera

Si se descarga el repositorio desde github:
git clone https://github.com/PatricioHenderson/todo-challenge

# launching
1. Dentro de la carpeta todo-chalenge ejecutar docker-compose up
2. En un nuevo terminal ejecutar docker exec -it invera bash
3. cd invera/invera 
4. Python manage.py makemigrations
5. Python manage.py migate
6. Python manage.py createsuperuser
7. Acceder a http://localhost:8000/admin e ingresar con el usuario y la contraseña creados en el paso anterior




# Invera ToDo-List Challenge (Python/Django Jr-SSr)


El propósito de esta prueba es conocer tu capacidad para crear una pequeña aplicación funcional en un límite de tiempo. A continuación, encontrarás las funciones, los requisitos y los puntos clave que debés tener en cuenta durante el desarrollo.

## Qué queremos que hagas:

- El Challenge consiste en crear una aplicación web sencilla que permita a los usuarios crear y mantener una lista de tareas.
- La entrega del resultado será en un nuevo fork de este repo y deberás hacer una pequeña demo del funcionamiento y desarrollo del proyecto ante un super comité de las más grandes mentes maestras de Invera, o a un par de devs, lo que sea más fácil de conseguir.
- Podes contactarnos en caso que tengas alguna consulta.

## Objetivos:

El usuario de la aplicación tiene que ser capaz de:

- Crear una tarea
- Eliminar una tarea
- Marcar tareas como completadas
- Poder ver una lista de todas las tareas existentes
- Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma

## Qué evaluamos:

- Desarrollo utilizando Python, Django. No es necesario crear un Front-End, pero sí es necesario tener una API que permita cumplir con los objetivos de arriba.
- Calidad y arquitectura de código. Facilidad de lectura y mantenimiento del código. Estándares seguidos.
- [Bonus] Manejo de logs.
- [Bonus] Creación de tests (unitarias y de integración)
- [Bonus] Unificar la solución propuesta en una imagen de Docker por repositorio para poder ser ejecutada en cualquier ambiente (si aplica para full stack).

## Requerimientos de entrega:

- Hacer un fork del proyecto y pushearlo en github. Puede ser privado.
- La solución debe correr correctamente.
- El Readme debe contener todas las instrucciones para poder levantar la aplicación, en caso de ser necesario, y explicar cómo se usa.
- Disponibilidad para realizar una pequeña demo del proyecto al finalizar el challenge.
- Tiempo para la entrega: Aproximadamente 7 días.
