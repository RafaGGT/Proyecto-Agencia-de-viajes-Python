import modelo.Usuario as usr
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
