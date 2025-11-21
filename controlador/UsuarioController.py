import servicio.UsuarioService as user
import re
from servicio.Conexion import Conexion


class UsurarioController:
    def __init__(self):
        self.__usuario = user.UsuarioService(Conexion())

    def nuevo_usuario(self, nombre, apellidos, nickname, email, telefono, rol_id, contrasena):
        if not nombre or not apellidos or not nickname or not email or not telefono or not rol_id or not contrasena:
            raise ValueError("Todos los campos son obligatorios.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("El formato del correo electrónico es inválido.")
        elif not re.match(r"^\+?\d{10,15}$", telefono):
            raise ValueError("El formato del número de teléfono es inválido.")
        elif len(contrasena) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        else:
            self.__usuario.registrar_usuario(nombre, apellidos, nickname, email, telefono, rol_id, contrasena)