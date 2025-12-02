import modelo.Usuario as usr

class UsuarioService:
    # Prepara el servicio con la conexion activa.
    def __init__(self, conexion):
        self.__conexion = conexion.obtener_conexion()

    # Registra un nuevo usuario validando duplicados y devolviendo el id generado.
    def registrar_usuario(self, nombre, apellidos, nickname, email, telefono, rol_id, contrasena):
        if self.usuario_por_email_o_nickname(email) or self.usuario_por_email_o_nickname(nickname):
            raise ValueError("Ya existe un usuario con el mismo email o apodo.")

        cursor = self.__conexion.cursor()
        try:
            usuario = usr.Usuario(
                nombre=nombre,
                apellidos=apellidos,
                nickname=nickname,
                email=email,
                telefono=telefono,
                rol_id=rol_id,
            )
            usuario.contrasena = contrasena

            consulta = """
                INSERT INTO usuarios (nombre, apellidos, nickname, email, clave, telefono, rol_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            datos = (
                usuario.nombre,
                usuario.apellidos,
                usuario.nickname,
                usuario.email,
                usuario.contrasena,
                usuario.telefono,
                usuario.rol_id,
            )
            cursor.execute(consulta, datos)
            self.__conexion.commit()
            return cursor.lastrowid
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    # Recupera un usuario a partir de su email o nickname.
    def usuario_por_email_o_nickname(self, valor):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                SELECT id, nombre, apellidos, nickname, email, clave, telefono, rol_id
                FROM usuarios
                WHERE email=%s OR nickname=%s
                LIMIT 1;
            """
            cursor.execute(consulta, (valor, valor))
            fila = cursor.fetchone()
            return usr.Usuario.desde_fila(fila)
        except Exception:
            return None
        finally:
            cursor.close()

    # Recupera un usuario por su identificador.
    def usuario_por_id(self, usuario_id):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                SELECT id, nombre, apellidos, nickname, email, clave, telefono, rol_id
                FROM usuarios
                WHERE id=%s
                LIMIT 1;
            """
            cursor.execute(consulta, (usuario_id,))
            fila = cursor.fetchone()
            return usr.Usuario.desde_fila(fila)
        except Exception:
            return None
        finally:
            cursor.close()

    # Valida las credenciales y retorna el usuario autenticado si corresponde.
    def autenticar(self, identificador, contrasena):
        usuario = self.usuario_por_email_o_nickname(identificador)
        if usuario and usuario.verificar_contrasena(contrasena):
            return usuario
        return None

    # Garantiza la existencia de un usuario administrador por defecto.
    def asegurar_administrador(self, rol_admin_id, email_admin, clave_admin):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute("SELECT id FROM usuarios WHERE rol_id=%s LIMIT 1;", (rol_admin_id,))
            existente = cursor.fetchone()
            if existente:
                return existente[0]

            nuevo_id = self.registrar_usuario(
                nombre="Administrador",
                apellidos="Viajes Aventura",
                nickname="admin",
                email=email_admin,
                telefono="+0000000000",
                rol_id=rol_admin_id,
                contrasena=clave_admin,
            )
            return nuevo_id
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    # Modifica un campo especifico del usuario mas no la clave.
    def modificar_usuario(self, id, tipo, dato):
        cursor = self.__conexion.cursor()
        consulta = f"UPDATE usuarios SET {tipo}=%s WHERE id=%s;"
        try:
            cursor.execute(consulta, (dato, id))
            self.__conexion.commit()
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    def cambiar_contrasena(self, id, vieja_contrasena, nueva_contrasena):
        cursor = self.__conexion.cursor()
        try:
            # Obtener usuario desde la BD
            consulta = """
                SELECT id, nombre, apellidos, nickname, email, clave, telefono, rol_id
                FROM usuarios
                WHERE id=%s
                LIMIT 1;
            """
            cursor.execute(consulta, (id,))
            fila = cursor.fetchone()
            if not fila:
                raise ValueError("Usuario no encontrado.")

            usuario = usr.Usuario.desde_fila(fila)

            # Verificar contraseña actual
            if not usuario.verificar_contrasena(vieja_contrasena):
                raise ValueError("La contraseña actual es incorrecta.")

            # Generar hash de la nueva contraseña y actualizar en BD
            usuario.contrasena = nueva_contrasena
            cursor.execute(
                "UPDATE usuarios SET clave=%s WHERE id=%s;",
                (usuario.contrasena, id)
            )
            self.__conexion.commit()
            return True
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    def eliminar_cuenta(self, id):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute("DELETE FROM usuarios WHERE id=%s;", (id,))
            self.__conexion.commit()
            return cursor.rowcount > 0
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()
