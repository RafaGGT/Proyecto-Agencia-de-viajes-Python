from datetime import datetime
from modelo.PaqueteTuristico import PaqueteTuristico
from servicio.PaqueteService import PaqueteService
from servicio.DestinoService import DestinoService


class PaqueteController:
    # Construye el controlador de paquetes con servicios compartidos.
    def __init__(self, conexion):
        self.__paquete_service = PaqueteService(conexion)
        self.__destino_service = DestinoService(conexion)

    # Crea un paquete turistico para un destino dado.
    def crear(self, destino_id, fecha_inicio, fecha_fin, precio_total=None, disponible=True):
        self.__validar_fechas(fecha_inicio, fecha_fin)
        destino = self.__destino_service.obtener_destino(destino_id)
        if not destino:
            raise ValueError("El destino indicado no existe.")

        paquete = PaqueteTuristico(
            destino_id=destino_id,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            precio_total=precio_total,
            disponible=disponible,
        )
        return self.__paquete_service.crear_paquete(paquete, costo_base_destino=destino.costo_base)

    # Lista todos los paquetes existentes.
    def listar(self):
        return self.__paquete_service.listar_paquetes()

    # Lista paquetes disponibles para un rango de fechas.
    def listar_disponibles(self, fecha_inicio, fecha_fin):
        self.__validar_fechas(fecha_inicio, fecha_fin)
        return self.__paquete_service.listar_disponibles_por_fecha(fecha_inicio, fecha_fin)

    # Actualiza la disponibilidad de un paquete.
    def actualizar_disponibilidad(self, paquete_id, disponible):
        return self.__paquete_service.actualizar_disponibilidad(paquete_id, disponible)

    # Obtiene un paquete por identificador.
    def obtener(self, paquete_id):
        return self.__paquete_service.obtener_paquete(paquete_id)

    # Confirma que las fechas tengan un formato valido y un rango correcto.
    def __validar_fechas(self, fecha_inicio, fecha_fin):
        try:
            inicio = datetime.strptime(str(fecha_inicio), "%Y-%m-%d")
            fin = datetime.strptime(str(fecha_fin), "%Y-%m-%d")
            if inicio > fin:
                raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        except ValueError:
            raise ValueError("Las fechas deben tener el formato AAAA-MM-DD.")
