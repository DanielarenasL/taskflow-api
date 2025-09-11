# Prueba Tecnica

## Descripcion

Esta es una prueba tecnica acerca de una api para control de proyectos, esta realizada en python con una conexion a una base de datos PostgreSQL que se encuentra hosteada en Render

## Funcionalidades

### User

#### Permite:
    -crear
    -listar 
    -actualizar usuarios

### Team

#### Permite: 
    -crear
    -obtener
    -actualizar
    -eliminar

### Project

#### Permite:
    -obtener
    -crear
    -actualizar
    -eliminar

### Task

#### Permite:
    -crear tarea
    -obtener tarea por id
    -actualizar tarea
    -eliminar tarea
    -asignar tarea

## Ejecucion en local

para ejecutarlo en local solo hay que escribir en la consola: 

    python -m uvicorn manage:app --reload   

esto servira esta url local: http://127.0.0.1:8000

a partir de ahi se puede testear la api

## Produccion

La API esta desplegada en render en esta url:

    https://taskflow-api-giq1.onrender.com
