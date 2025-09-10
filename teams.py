from typing import final
from connection import connection

def create_team(name, description, lead_user):
    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        cursor = conn.cursor()
        
        # Verificar si el usuario ya existe usando parámetros preparados
        cursor.execute("SELECT id FROM team WHERE name = %s ", (name,))
        existing_team = cursor.fetchone()
        if existing_team:
            print(f"El equipo '{name}' ya existe")
            return False

        # Insertar nuevo usuario usando parámetros preparados
        cursor.execute(
            "INSERT INTO team (name, description, lead_user ) VALUES (%s, %s, %s)",
            (name, description, lead_user)
        )
        
        conn.commit()
        print(f"Equipo '{name}' creado exitosamente")
        return True
    except Exception as e:
        print(f"Error al crear el equipo: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_teams():
    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM team")
        teams = cursor.fetchall()
        print(teams)
        return teams
    except Exception as e:
        print(f"Error al obtener equipos: {e}")
        return False
    finally:
        if cursor: 
            cursor.close()
        if conn:
            conn.close()

def update_team(id, field, new_data):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False
        
        cursor = conn.cursor()

        if field == "name":
            cursor.execute("SELECT * FROM team WHERE id = %s", (id,))
            existing_name = cursor.fetchone()
            print(existing_name)
        if existing_name and existing_name[1] == new_data:
            print(f"El nombre del equipo es el mismo que el actual")
            return False
        
        cursor.execute(f"UPDATE team SET {field} = %s WHERE id = %s", (new_data, id,))
        conn.commit()
        print(f"El campo {field} se actualizo correctamente")
        return 
    except Exception as e:
        print(f"Error al actualizar el equipo: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn: 
            conn.close()

# def get_members(team_id):
#     conn = None
#     cursor = None


def add_member(team_name, member_id):
    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False


        cursor = conn.cursor()

        cursor.execute("SELECT id FROM team WHERE name = %s", (team_name,))
        existing_team = cursor.fetchone()
        if not existing_team:
            print(f"El equipo '{team_name}' no existe ")

        cursor.execute("SELECT * FROM members WHERE user_id = %s", (member_id,))
        existing_member = cursor.fetchone()
        if existing_member:
            print(f"El usuario ya es miembro de este equipo")
            return False

        cursor.execute("INSERT INTO members (team_id, user_id) VALUES (%s, %s)", (existing_team[0], member_id,))
        conn.commit()
        print("miembro agregado exitosamente")
        return True
    except Exception as e:
        print(f"Error al agregar usuario: {e}")
        return False
    finally: 
        if cursor:
            cursor.close()
        if conn: 
            conn.close()
