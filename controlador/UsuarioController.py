import servicio.UsuarioService as user
import re
from servicio.Conexion import Conexion


class UsurarioController:
    def __init__(self):
        self.__usuario = user.UsuarioService(Conexion())

    def nuevo_usuario(self, nombre, apellidos, nickname, email, telefono, rol_id, contrasena):
        if not nombre or not apellidos or not nickname or not email or not telefono or not rol_id or not contrasena:
            print("Todos los campos son obligatorios.")
            return
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("El formato del correo electrónico es inválido.")
            return
        elif not re.match(r"^\+?\d{8,9}$", telefono):
            print("El formato del número de teléfono es inválido.")
            return
        elif len(contrasena) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
            return
        elif rol_id != 1 and rol_id != 2:
            print("El ID de rol debe ser 1 (Usuario) o 2 (Administrador).")
            return
        else:
            self.__usuario.registrar_usuario(nombre, apellidos, nickname, email, telefono, rol_id, contrasena)

    def autenticar_usuario(self, nickname, contrasena):
        if not nickname or not contrasena:
            print("El nombre de usuario y la contraseña son obligatorios.")
            return None
        else: 
            sesion = self.__usuario.autenticar_usuario(nickname, contrasena)
            if sesion:
                print("Autenticación exitosa.")
                return sesion
            else:
                print("Nombre de usuario o contraseña incorrectos.")
                return None