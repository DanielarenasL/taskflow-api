from connection import connection


def create_project(name, description, team_id, status, start_date, end_date, priority):
    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        cursor = conn.cursor()

        cursor.execute("SELECT id FROM project WHERE name = %s", (name,))
        existing_project = cursor.fetchone()
        if existing_project:
            print(f"El proyecto {name} ya existe")
            return False
        
        cursor.execute(
            "INSERT INTO project (name, description, team_id, status, start_date, end_date, priority) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, description, team_id, status, start_date, end_date, priority)
        )
        
        conn.commit()
        print(f"El proyecto {name} se creó correctamente")
        return True
    except Exception as e:
        print(f"Error al crear proyecto: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_project(project_id):
    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        cursor = conn.cursor()

        cursor.execute("SELECT name FROM project WHERE id = %s", (project_id,))
        existing_project = cursor.fetchone()

        if not existing_project:
            print("El proyecto no existe")
            return False
        
        cursor.execute("DELETE FROM project WHERE id = %s", (project_id,))
        conn.commit()
        print("Proyecto eliminado correctamente")
        return True
    except Exception as e:
        print(f"Error al eliminar proyecto: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_project(project_id, field, new_value):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False
        
        cursor = conn.cursor()

        if field == "name":
            cursor.execute("SELECT * FROM project WHERE id = %s", (project_id,))
            existing_name = cursor.fetchone()

            if existing_name and existing_name[1] == new_value:
                print("El nombre del proyecto es el mismo que el actual")
                return False

        elif field == "team_id":
            cursor.execute("SELECT name FROM team WHERE id = %s", (new_value,))
            existing_team = cursor.fetchone()
            if not existing_team and field == "team_id":
                return False
            
        
        
        cursor.execute(f"UPDATE project SET {field} = %s WHERE id = %s", (new_value, project_id,))
        conn.commit()
        print(f"El campo {field} se actualizo correctamente")
        return True
    except Exception as e:
        print(f"Error al actualizar el proyecto: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn: 
            conn.close()

def get_projects_filtered(field, filter):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False
        
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM project WHERE {field} = %s", (filter,))
        projects = cursor.fetchall()
        print(projects)
        return projects
    except Exception as e:
        print(f"Error al obtener proyectos: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()