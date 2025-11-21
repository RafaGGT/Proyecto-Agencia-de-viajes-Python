import modelo.Usuario as usr
import bcrypt
class UsuarioService:
    def __init__(self, conexion):
        self.__conexion = conexion.obtener_conexion()

    def registrar_usuario(self, nombre, apellidos, nickname, email, telefono, rol_id, contrasena):
        try:
            cursor = self.__conexion.cursor()
            usuario = usr.Usuario(
                nombre=nombre,
                apellidos=apellidos,
                nickname=nickname,
                email=email,
                telefono=telefono,
                rol_id=rol_id,
                contrasena=contrasena 
            )
            # Usar el setter para que quede hasheada
            usuario.contrasena = contrasena 
            consulta= """INSERT INTO usuarios (nombre, apellidos, nickname, email, clave, telefono, rol_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s);"""
            datos = (
                usuario.nombre,
                usuario.apellidos,
                usuario.nickname,
                usuario.email,
                usuario.contrasena,
                usuario.telefono,
                usuario.rol_id
            )
            cursor.execute(consulta, datos)
            self.__conexion.commit()
            cursor.close()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al contactar la base de datos: {e}")
            return None

    def autenticar_usuario(self, nickname, contrasena):
        try:
            cursor = self.__conexion.cursor()
            consulta = "SELECT id, nombre, apellidos, nickname, email, clave, telefono, rol_id FROM usuarios WHERE nickname = %s;"
            cursor.execute(consulta, (nickname,))
            fila = cursor.fetchone()
            cursor.close()
            if fila:
                id_db, nombre_db, apellidos_db, nickname_db, email_db, clave_db, telefono_db, rol_id_db = fila
            elif not fila:
                return False
            if bcrypt.checkpw(contrasena.encode('utf-8'), clave_db.encode('utf-8')):
                Usuario = usr.Usuario(
                    id=id_db,
                    nombre=nombre_db,
                    apellidos=apellidos_db,
                    nickname=nickname_db,
                    email=email_db,
                    telefono=telefono_db,
                    rol_id=rol_id_db
                )
                return Usuario
            else:
                return False
        except Exception as e:
            print("Error de conexion, intente mas tarde.", e)
            return False

