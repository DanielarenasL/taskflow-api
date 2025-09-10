from connection import connection

def create_user(name, description, lead_user, members):
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
            "INSERT INTO team (name, description, lead_user, members, ) VALUES (%s, %s, %s, %s, %s)",
            (name, description, lead_user, members)
        )
        
        conn.commit()
        print(f"Equipo '{name}' creado exitosamente")
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
