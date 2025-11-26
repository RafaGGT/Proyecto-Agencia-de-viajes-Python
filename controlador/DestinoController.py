from modelo.Destino import Destino
from servicio.DestinoService import DestinoService


class DestinoController:
    # Prepara el controlador con el servicio de destinos.
    def __init__(self, conexion):
        self.__service = DestinoService(conexion)

    # Crea un destino luego de validar los datos requeridos.
    def crear(self, nombre, descripcion, actividades, costo_base):
        self.__validar(nombre, costo_base)
        destino = Destino(
            nombre=nombre,
            descripcion=descripcion,
            actividades=actividades,
            costo_base=costo_base,
        )
        return self.__service.crear_destino(destino)

    # Devuelve todos los destinos existentes.
    def listar(self):
        return self.__service.listar_destinos()

    # Actualiza un destino existente.
    def actualizar(self, destino_id, cambio, tipo):
        return self.__service.actualizar_destino(destino_id, cambio, tipo)

    # Elimina un destino por su identificador.
    def eliminar(self, destino_id):
        if not str(destino_id).isdigit():
            raise ValueError("El ID de destino debe ser un número válido.")
        destino_id = int(destino_id)
        return self.__service.eliminar_destino(destino_id)

    # Obtiene un destino especifico.
    def obtener(self, destino_id):
        return self.__service.obtener_destino(destino_id)

    # Valida los campos minimos de un destino.
    def __validar(self, nombre, costo_base):
        if not nombre:
            raise ValueError("El destino debe tener un nombre.")
        if costo_base is None or float(costo_base) < 0:
            raise ValueError("El costo base debe ser mayor o igual a cero.")
