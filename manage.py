from fastapi import FastAPI, HTTPException, Request
from apps.teams import *
from apps.projects import *
from apps.tasks import *
from apps.users import *


app = FastAPI()

@app.get("/api/users/")
def list_users_endpoint():

    users = get_users()
    if not users:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")

    return users

@app.get("/api/users/{id}")
def get_user_by_id_endpoint(id: str):

    user = get_user_by_id(id)
    if not user: 
        raise HTTPException(status_code=404, detail="Usuario no encontrados")

    return user
 
@app.put("/api/users/{id}")
async def update_user_endpoint(id: str, request: Request):
    body = await request.json()

    data = body.get("data")
    new_data = body.get("new_data")

    result = update_user(id, data, new_data)

    if not result:
        raise HTTPException(status_code=404, detail="Error al actualizar usuario")

    return result

#! Arreglar
@app.get("/api/users/me/")
async def get_my_user_endpoint(request: Request):

    body = await request.json()

    my_id = body.get("id")

    result = get_user_by_id(my_id)

    if not result:
        raise HTTPException(status_code=404, detail="Error al encontrar el usuario")
    
    return result

#* ----------------------Teams------------------------


@app.get("/api/teams/")
def get_teams_endpoint():

    teams = get_teams()
    if not teams:
        raise HTTPException(status_code=404, detail="Equipos no encontrados")

    return teams

@app.post("/api/teams/")
async def create_team_endpoint(request: Request):

    body = await request.json()

    name = body.get("name")
    description = body.get("description")
    lead_user = body.get("lead_user")

    result = create_team(name, description, lead_user)

    if not result:
        raise HTTPException(status_code=404, detail="Error al crear el equipo")

    return result

#! Arreglar
# @app.get("/api/teams/{id}")
# def get_team_and_members_endpoint():



#     if not result:
#         raise HTTPException(status_code=404, detail="Error al crear el equipo")

@app.put("/api/teams/{id}")
async def update_team_endpoint(id: str, request: Request):
    
    body = await request.json()

    field = body.get("field")
    new_data = body.get("new_data")

    result = update_team(id, field, new_data)

    if not result:
        raise HTTPException(status_code=404, detail="Error al actualizar el equipo")

    return result

@app.delete("/api/teams/{id}")
def delete_team_endpoint(id: str):

    return delete_team(id)

#* --------------------------Project----------------------

#! Arreglar 
@app.get("/api/projects/")
async def get_projects_endpoint(request: Request):

    body = await request.json()

    field = body.get("field")
    filters = body.get("filters")

    result = get_projects_filtered(field, filters)

    if not result:
        raise HTTPException(status_code=404, detail="Error al obtener los proyectos")
    
    return result


@app.post("/api/projects/")
async def create_project_endpoint(request: Request):

    body = await request.json()

    name = body.get("name")
    description = body.get("description")
    team_id = body.get("team_id")
    status = body.get("status")
    start_date = body.get("start_date")
    end_date = body.get("end_date")
    priority = body.get("priority")

    result = create_project(name, description, team_id, status, start_date, end_date, priority)

    if not result:
        raise HTTPException(status_code=404, detail="Error al crear el proyecto")
    
    return result


@app.put("/api/projects/{id}")
async def update_project_endpoint(id: str, request: Request):
    body = await request.json()

    field = body.get("field")
    new_value = body.get("new_value")
    result = update_project(id, field, new_value)

    if not result:
        raise HTTPException(status_code=404, detail="Error al actualizar el proyecto")
    
    return {"mensaje": f"El campo {field} se actualizó correctamente"}

@app.delete("/api/projects/{id}")
def delete_project_endpoint(id: str):

    resultado = delete_project(id)
    
    if not resultado:
        raise HTTPException(status_code=404, detail="Error al eliminar el proyecto")

    return {"mensaje": "Proyecto eliminado correctamente"}

#* --------------------------Tasks--------------------

@app.post("/api/tasks/")
async def create_task_endpoint(request: Request):
    body = await request.json()

    title = body.get("title")
    description = body.get("description")
    project_id = body.get("project_id")
    created_by = body.get("created_by")
    status = body.get("status")
    priority = body.get("priority")
    estimated_hours = body.get("estimated_hours")
    actual_hours = body.get("actual_hours")
    due_date = body.get("due_date")
    tags = body.get("tags")

    result = create_task(
        title,
        description,
        project_id,
        created_by,
        status,
        priority,
        estimated_hours,
        actual_hours,
        due_date,
        tags
    )

    if not result:
        raise HTTPException(status_code=404, detail="Error al crear la tarea")
    
    return {"mensaje": "Tarea creada correctamente"}

@app.get("/api/tasks/{id}")
def get_task_by_id_endpoint(id: str):

    task = get_task_by_id(id)

    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return task

@app.put("/api/tasks/{id}")
async def uptate_task_endpoint(id: str, request: Request):

    body = await request.json()

    field = body.get("field")
    new_data = body.get("new_data")

    result = update_task(id, field, new_data)

    if not result:
        raise HTTPException(status_code=404, detail="Error al crear la tarea")

    return {"mensaje": "Tarea actualizada correctamente"}


@app.delete("/api/tasks/{id}")
def delete_task_endpoint(id: str):

    result = delete_task(id)

    if not result:
        raise HTTPException(status_code=404, detail="Error al eliminar la tarea")

    return {"mensaje": "Tarea eliminada correctamente"}

@app.post("/api/tasks/{id}/assign/")
async def assign_task_endpoint(id: str, request: Request):

    body = await request.json()

    user_id = body.get("user_id")

    result = assign_task(id, user_id)

    if not result:
        raise HTTPException(status_code=404, detail="Error al asignar la tarea")

    return {"mensaje": "Tarea asignada correctamente"}

#! 