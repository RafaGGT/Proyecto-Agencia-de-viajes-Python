import re
import servicio.UsuarioService as user
from servicio.Conexion import Conexion
from servicio.RolService import RolService
from servicio.ReservaService import ReservaService


class UsuarioController:
    # Construye el controlador y levanta las dependencias de servicios.
    def __init__(self, conexion=None):
        self.__conexion = conexion or Conexion()
        self.__usuario_service = user.UsuarioService(self.__conexion)
        self.__rol_service = RolService(self.__conexion)
        self.__reserva_service = ReservaService(self.__conexion)

    # Registra un nuevo usuario luego de validar los campos requeridos.
    def nuevo_usuario(self, nombre, apellidos, nickname, email, telefono, rol_id, contrasena):
        self.__validar_campos(nombre, apellidos, nickname, email, telefono, contrasena)
        return self.__usuario_service.registrar_usuario(
            nombre=nombre,
            apellidos=apellidos,
            nickname=nickname,
            email=email,
            telefono=telefono,
            rol_id=rol_id,
            contrasena=contrasena,
        )

    # Autentica al usuario usando email o nickname mas la contraseña.
    def autenticar(self, identificador, contrasena):
        return self.__usuario_service.autenticar(identificador, contrasena)

    # Devuelve el usuario por identificador.
    def obtener_usuario(self, usuario_id):
        return self.__usuario_service.usuario_por_id(usuario_id)

    # Garantiza roles y estados iniciales junto con la creacion del administrador.
    def asegurar_datos_iniciales(self):
        roles = self.__rol_service.crear_roles_basicos()
        estados = self.__reserva_service.asegurar_estados()
        admin_mail = "admin@viajesaventura.com"
        admin_pass = "12345678"
        self.__usuario_service.asegurar_administrador(roles["admin"], admin_mail, admin_pass)
        return {"roles": roles, "estados": estados}

    # Verifica la consistencia de los campos del usuario.
    def __validar_campos(self, nombre, apellidos, nickname, email, telefono, contrasena):
        if not nombre or not apellidos or not nickname or not email or not telefono or not contrasena:
            raise ValueError("Todos los campos son obligatorios.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("El formato del correo electrónico es inválido.")
        if not re.match(r"^\+?\d{7,15}$", telefono):
            raise ValueError("El formato del número de teléfono es inválido.")
        if len(contrasena) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
