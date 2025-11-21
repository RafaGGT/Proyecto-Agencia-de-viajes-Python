class PaqueteTuristico:
    # Inicializa un paquete turistico con referencias al destino y fechas definidas.
    def __init__(self, id=None, destino_id=None, fecha_inicio=None, fecha_fin=None, precio_total=0.0, disponible=True):
        self.__id = id
        self.__destino_id = destino_id
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__precio_total = precio_total
        self.__disponible = disponible

    # Devuelve el identificador del paquete.
    @property
    def id(self):
        return self.__id

    # Devuelve el identificador del destino asociado.
    @property
    def destino_id(self):
        return self.__destino_id

    # Asigna el identificador del destino asociado.
    @destino_id.setter
    def destino_id(self, valor):
        self.__destino_id = valor

    # Devuelve la fecha de inicio del paquete.
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    # Asigna la fecha de inicio del paquete.
    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self.__fecha_inicio = valor

    # Devuelve la fecha de fin del paquete.
    @property
    def fecha_fin(self):
        return self.__fecha_fin

    # Asigna la fecha de fin del paquete.
    @fecha_fin.setter
    def fecha_fin(self, valor):
        self.__fecha_fin = valor

    # Devuelve el precio total calculado para el paquete.
    @property
    def precio_total(self):
        return self.__precio_total

    # Asigna el precio total del paquete.
    @precio_total.setter
    def precio_total(self, valor):
        self.__precio_total = valor

    # Indica si el paquete esta disponible.
    @property
    def disponible(self):
        return self.__disponible

    # Marca la disponibilidad del paquete.
    @disponible.setter
    def disponible(self, valor):
        self.__disponible = valor
