import bcrypt

class Usuario:
    def __init__(self, id=None, nombre=None, apellidos=None, nickname=None, email=None, telefono=None, rol_id=None, contrasena=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__nickname = nickname
        self.__email = email
        self.__telefono = telefono
        self.__rol_id = rol_id    
        self.__contrasena = contrasena

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self.__apellidos = valor

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, valor):
        self.__nickname = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        self.__telefono = valor

    @property
    def rol_id(self):
        return self.__rol_id

    @rol_id.setter
    def rol_id(self, valor):
        self.__rol_id = valor

    @property 
    def contrasena(self): 
        return self.__contrasena
    
    @contrasena.setter
    def contrasena(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("La contraseña no puede estar vacía.")
        hash_contrasena = bcrypt.hashpw( valor.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') 
        self.__contrasena = hash_contrasena