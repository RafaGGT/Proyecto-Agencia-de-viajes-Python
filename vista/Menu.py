from controlador.UsuarioController import UsurarioController as uCont
import pwinput
import os 
class Menu:
    def __init__(self):
        self.__controlador = uCont()       
        self.__usuario_actual = None

    def mostrar_menu(self):
        os.system('cls')
        print("=== Menú Inicio ===")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opciones = {"1": self.registrar_usuario, 
                    "2": self.iniciarSesion}
        opcion = input("Seleccione una opción: ")
        if opcion == "3":
            print("Saliendo del programa...")
            return
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            self.mostrar_menu()

    def registrar_usuario(self):
        print("=== Registro de Usuario ===")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        nickname = input("Nickname: ")
        email = input("Email: ")
        telefono = input("Teléfono: ")
        print("Roles disponibles: \n 1. Usuario \n 2. Administrador")
        rol_id = int(input("ID de Rol: "))
        contrasena = pwinput.pwinput("Contraseña: ", mask="*")
        controlador = self.__controlador
        controlador.nuevo_usuario(nombre, apellidos, nickname, email, telefono, rol_id, contrasena)
        input("Usuario registrado exitosamente, presiona enter para continuar...")
        self.mostrar_menu()
        
    def iniciarSesion(self):
        print("=== Iniciar Sesión ===")
        nombreDeUsuario = input("Nombre de usuario: ").strip()
        contrasena = pwinput.pwinput("Ingrese la contraseña: ", mask = "*").strip()
        try:
            controlador = self.__controlador
            usuario = controlador.autenticar_usuario(nombreDeUsuario, contrasena)
            if usuario:
                # guardar el objeto Usuario devuelto
                self.__usuario_actual = usuario
                print("Inicio de sesión exitoso.")
                input("Presiona enter para continuar...")
                self.lobby()
            else:
                self.__usuario_actual = None
                print("Nombre de usuario o contraseña incorrectos.")
                input("Presiona enter para continuar...")
                self.mostrar_menu()
        except Exception as e:
            print(f"Error al autenticar el usuario: {e}")
            input("Presiona enter para continuar...")
            self.mostrar_menu()
        
    def lobby(self):
        print(f"=== Bienvenido {self.__usuario_actual.nombre} ===")