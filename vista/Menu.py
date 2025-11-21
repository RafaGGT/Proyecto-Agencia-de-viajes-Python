from controlador.UsuarioController import UsurarioController as uCont
import pwinput
class Menu:
    def __init__(self):
        self.__controlador = uCont()       
        self.__usuario_actual = None

    def mostrar_menu(self):
        while True:
            print("=== Menú Inicio ===")
            print("1. Registrar Usuario")
            print("2. Iniciar Sesión")
            print("3. Salir")
            opciones = {"1": self.registrar_usuario}
            while True:
                opcion = input("Seleccione una opción: ")
                if opcion == "3":
                    print("Saliendo del programa...")
                    return
                elif opcion in opciones:
                    opciones[opcion]()
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")

    def registrar_usuario(self):
        print("Registro de Usuario")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        nickname = input("Nickname: ")
        email = input("Email: ")
        telefono = input("Teléfono: ")
        rol_id = int(input("ID de Rol: "))
        contrasena = pwinput.pwinput("Contraseña: ", mask="*")
        controlador = self.__controlador
        controlador.nuevo_usuario(nombre, apellidos, nickname, email, telefono, rol_id, contrasena)
        input("Usuario registrado exitosamente, presiona enter para continuar...")
        
