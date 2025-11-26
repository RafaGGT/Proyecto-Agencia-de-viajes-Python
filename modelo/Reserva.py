class Reserva:
    # Inicializa una reserva con referencias a usuario, paquete y estado.
    def __init__(self, id=None, usuario_id=None, paquete_id=None, estado_id=None, fecha_reserva=None):
        self.__id = id
        self.__usuario_id = usuario_id
        self.__paquete_id = paquete_id
        self.__estado_id = estado_id
        self.__fecha_reserva = fecha_reserva

    # Devuelve el identificador de la reserva.
    @property
    def id(self):
        return self.__id

    # Devuelve el identificador del usuario que reservo.
    @property
    def usuario_id(self):
        return self.__usuario_id

    # Asigna el identificador del usuario que reservo.
    @usuario_id.setter
    def usuario_id(self, valor):
        self.__usuario_id = valor

    # Devuelve el identificador del paquete reservado.
    @property
    def paquete_id(self):
        return self.__paquete_id

    # Asigna el identificador del paquete reservado.
    @paquete_id.setter
    def paquete_id(self, valor):
        self.__paquete_id = valor

    # Devuelve el identificador del estado de la reserva.
    @property
    def estado_id(self):
        return self.__estado_id

    # Asigna el identificador del estado de la reserva.
    @estado_id.setter
    def estado_id(self, valor):
        self.__estado_id = valor

    # Devuelve la fecha y hora de la reserva.
    @property
    def fecha_reserva(self):
        return self.__fecha_reserva

    # Asigna la fecha y hora de la reserva.
    @fecha_reserva.setter
    def fecha_reserva(self, valor):
        self.__fecha_reserva = valor
