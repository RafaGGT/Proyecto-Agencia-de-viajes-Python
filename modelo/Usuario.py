import bcrypt

class Usuario:
    # Crea una nueva instancia de usuario con la informacion basica y opcionalmente con el id y la clave ya hasheada.
    def __init__(self, id=None, nombre=None, apellidos=None, nickname=None, email=None, telefono=None, rol_id=None, contrasena=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__nickname = nickname
        self.__email = email
        self.__telefono = telefono
        self.__rol_id = rol_id
        self.__contrasena = contrasena

    # Devuelve el identificador interno del usuario.
    @property
    def id(self):
        return self.__id

    # Devuelve el nombre del usuario.
    @property
    def nombre(self):
        return self.__nombre

    # Asigna el nombre del usuario.
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    # Devuelve los apellidos del usuario.
    @property
    def apellidos(self):
        return self.__apellidos

    # Asigna los apellidos del usuario.
    @apellidos.setter
    def apellidos(self, valor):
        self.__apellidos = valor

    # Devuelve el apodo del usuario.
    @property
    def nickname(self):
        return self.__nickname

    # Asigna el apodo del usuario.
    @nickname.setter
    def nickname(self, valor):
        self.__nickname = valor

    # Devuelve el email del usuario.
    @property
    def email(self):
        return self.__email

    # Asigna el email del usuario.
    @email.setter
    def email(self, valor):
        self.__email = valor

    # Devuelve el telefono del usuario.
    @property
    def telefono(self):
        return self.__telefono

    # Asigna el telefono del usuario.
    @telefono.setter
    def telefono(self, valor):
        self.__telefono = valor

    # Devuelve el id del rol asociado al usuario.
    @property
    def rol_id(self):
        return self.__rol_id

    # Asigna el id del rol asociado al usuario.
    @rol_id.setter
    def rol_id(self, valor):
        self.__rol_id = valor

    # Devuelve la contraseña hasheada del usuario.
    @property
    def contrasena(self):
        return self.__contrasena

    # Asigna la contraseña generando un hash seguro.
    @contrasena.setter
    def contrasena(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("La contraseña no puede estar vacía.")
        hash_contrasena = bcrypt.hashpw(valor.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        self.__contrasena = hash_contrasena

    # Verifica si la contraseña en texto plano coincide con el hash almacenado.
    def verificar_contrasena(self, valor_plano):
        if self.__contrasena is None:
            return False
        try:
            return bcrypt.checkpw(valor_plano.encode("utf-8"), self.__contrasena.encode("utf-8"))
        except ValueError:
            return False

    # Construye un usuario a partir de una fila retornada por la base de datos.
    @staticmethod
    def desde_fila(fila):
        if not fila:
            return None
        return Usuario(
            id=fila[0],
            nombre=fila[1],
            apellidos=fila[2],
            nickname=fila[3],
            email=fila[4],
            telefono=fila[6],
            rol_id=fila[7],
            contrasena=fila[5],
        )
