class Destino:
    # Inicializa un destino con datos basicos y opcionalmente con su identificador.
    def __init__(self, id=None, nombre=None, descripcion=None, actividades=None, costo_base=0.0):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__actividades = actividades
        self.__costo_base = costo_base

    # Devuelve el identificador unico del destino.
    @property
    def id(self):
        return self.__id

    # Devuelve el nombre del destino.
    @property
    def nombre(self):
        return self.__nombre

    # Asigna el nombre del destino.
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    # Devuelve la descripcion del destino.
    @property
    def descripcion(self):
        return self.__descripcion

    # Asigna la descripcion del destino.
    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    # Devuelve las actividades asociadas al destino.
    @property
    def actividades(self):
        return self.__actividades

    # Asigna las actividades asociadas al destino.
    @actividades.setter
    def actividades(self, valor):
        self.__actividades = valor

    # Devuelve el costo base del destino.
    @property
    def costo_base(self):
        return self.__costo_base

    # Asigna el costo base del destino.
    @costo_base.setter
    def costo_base(self, valor):
        self.__costo_base = valor
