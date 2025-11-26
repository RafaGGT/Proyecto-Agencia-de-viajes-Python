class RolService:
    # Inicia el servicio con la conexion proporcionada.
    def __init__(self, conexion):
        self.__conexion = conexion.obtener_conexion()

    # Crea el rol si no existe y devuelve su id.
    def crear_rol_si_no_existe(self, nombre):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute("SELECT id FROM roles WHERE nombre=%s LIMIT 1;", (nombre,))
            encontrado = cursor.fetchone()
            if encontrado:
                return encontrado[0]
            cursor.execute("INSERT INTO roles (nombre) VALUES (%s);", (nombre,))
            self.__conexion.commit()
            return cursor.lastrowid
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    # Crea los roles basicos admin y cliente devolviendo un diccionario con sus ids.
    def crear_roles_basicos(self):
        admin_id = self.crear_rol_si_no_existe("admin")
        cliente_id = self.crear_rol_si_no_existe("cliente")
        return {"admin": admin_id, "cliente": cliente_id}
