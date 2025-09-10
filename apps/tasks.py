from connection import connection

def create_task(title, description, project_id, created_by, status, priority, estimated_hours, actual_hours, due_date, tags):

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
            print(f"el proyecto no existe")
            return False

        #! Hacer que en el endpoint verifique si el usuario pertenece al grupo
        

        cursor.execute("SELECT username FROM users WHERE id = %s", (created_by,))
        existing_creator = cursor.fetchone()
        if not existing_creator:
            print(f"el usuario no existe")
            return False

        cursor.execute("INSERT INTO task (title, description, project_id, created_by, status, priority, estimated_hours, actual_hours, due_date, tags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (title, description, project_id, created_by, status, priority, estimated_hours, actual_hours, due_date, tags)
        )

        conn.commit()
        print(f"La tarea '{title}' ha sido creada")
        return True
    except Exception as e:
        print(f"Error al crear la tarea: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_task_by_id(task_id):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM task WHERE id = %s", (task_id,))
        task = cursor.fetchone()

        if not task:
            print("La tarea no existe")
            return False

        print(task)
        return task

    except Exception as e:
        print(f"Error al obtener tarea: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_task(task_id):
    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        cursor = conn.cursor()

        cursor.execute("SELECT title FROM task WHERE id = %s", (task_id,))
        task = cursor.fetchone()
        if not task:
            print("La tarea no existe")
            return False
        
        cursor.execute("DELETE FROM task WHERE id = %s", (task_id,))
        conn.commit()
        print("La tarea ha sido eliminada")
        return True
    except Exception as e:
        print(f"Error al eliminar tarea: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def assign_task(task_id, user_id):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False
        
        cursor = conn.cursor()

        cursor.execute("SELECT username FROM users WHERE id = %s", (user_id,))
        existing_user = cursor.fetchone()
        if not existing_user:
            print("El usuario no existe")
            return False

        cursor.execute("SELECT id FROM task WHERE id = %s", (task_id,))
        existing_task = cursor.fetchone()
        if not existing_task:
            print("La tarea no existe")
            return False

        cursor.execute("UPDATE task SET assigned_to = %s WHERE id = %s", (user_id, task_id))
        conn.commit()
        print(f"La tarea fue asignada al usuario {existing_user[0]}")
        return True
    except Exception as e:
        print(f"Error al asignar tarea: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn: 
            conn.close()

def get_user_tasks(user_id):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if not user:
            print("El usuario no existe")
            return False
        
        cursor.execute("SELECT * FROM task WHERE assigned_to = %s", (user_id,))
        tasks = cursor.fetchall()
        print(tasks)
        return tasks
    except Exception as e:
        print(f"Error al obtener tareas: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_task(task_id, field, new_data):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False
        
        cursor = conn.cursor()

        if field == "assigned_to" or field == "created_by":
            print(f"No se permite modificar el campo {field}")
            return False

        cursor.execute("SELECT title FROM task WHERE id = %s", (task_id,))
        existing_task = cursor.fetchone()
        if not existing_task:
            print("La tarea no existe")
            return False
        
        cursor.execute(f"UPDATE task SET {field} = %s WHERE id = %s", (new_data, task_id,))
        conn.commit()
        print(f"El fampo {field} ha sido modificado")
        return True
    except Exception as e:
        print(f"Error al actualizar la tarea: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn: 
            conn.close()

def get_task_filtered(field, filter):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False
        
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM task WHERE {field} = %s", (filter,))
        tasks = cursor.fetchall()
        return tasks
    except Exception as e:
        print(f"Error al obtener tareas: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()