from servicio.ReservaService import ReservaService
from servicio.PaqueteService import PaqueteService


class ReservaController:
    # Prepara el controlador de reservas con servicios auxiliares.
    def __init__(self, conexion):
        self.__reserva_service = ReservaService(conexion)
        self.__paquete_service = PaqueteService(conexion)
        self.__estados = self.__reserva_service.asegurar_estados()

    # Genera una reserva si el paquete esta disponible.
    def crear_reserva(self, usuario_id, paquete_id):
        paquete = self.__paquete_service.obtener_paquete(paquete_id)
        if not paquete:
            raise ValueError("El paquete seleccionado no existe.")
        if not paquete.disponible:
            raise ValueError("El paquete no se encuentra disponible.")

        reserva_id = self.__reserva_service.crear_reserva(
            usuario_id,
            paquete_id,
            self.__estados.get("confirmada"),
        )
        self.__paquete_service.actualizar_disponibilidad(paquete_id, False)
        return reserva_id

    # Devuelve las reservas de un usuario especifico.
    def listar_reservas_usuario(self, usuario_id):
        return self.__reserva_service.listar_reservas_usuario(usuario_id)

    # Lista todas las reservas para los administradores.
    def listar_todas(self):
        return self.__reserva_service.listar_todas()
