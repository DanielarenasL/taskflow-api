from connection import connection


def create_user(username, email, first_name, last_name, role):
    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        cursor = conn.cursor()
        
        # Verificar si el usuario ya existe usando parámetros preparados
        cursor.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
        existing_user = cursor.fetchone()
        if existing_user:
            print(f"El usuario '{username}' o email '{email}' ya existe")
            return False

        # Insertar nuevo usuario usando parámetros preparados
        cursor.execute(
            "INSERT INTO users (username, email, first_name, last_name, role) VALUES (%s, %s, %s, %s, %s)",
            (username, email, first_name, last_name, role)
        )
        
        conn.commit()
        print(f"Usuario '{username}' creado exitosamente")
        return True
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_users():

    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)
        return users
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_user_by_id(id):
    conn = None
    cursor = None
    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        if not id:
            print("No se recibio un id valido")
            return False

        

        print(id)
        
        cursor = conn.cursor()
        #* los datetime hay que convertirlos a UTC
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()
        print(user)
        return user
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_user(id, data, new_data):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn is None:
            print("No se pudo establecer conexión a la base de datos")
            return False

        if not id:
            print("No se recibio un id valido")
            return False

        cursor = conn.cursor()


        cursor.execute("SELECT id FROM users WHERE id = %s ", (id,))
        existing_user = cursor.fetchone()
        if not existing_user:
            print(f"El usuario de id {id} no existe")
            return False


        cursor.execute(f"UPDATE users SET {data} = %s WHERE id = %s", (new_data, id,))
        conn.commit()
        print(f"El usuario de id {id} fue actualizado")
        return 

    except Exception as e:
        print(f"Error al editar el usuario: {e}")
        return False 
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        

