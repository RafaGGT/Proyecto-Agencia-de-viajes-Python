from datetime import datetime
import pwinput
from controlador.UsuarioController import UsuarioController
from controlador.DestinoController import DestinoController
from controlador.PaqueteController import PaqueteController
from controlador.ReservaController import ReservaController
from servicio.Conexion import Conexion


class Menu:
    # Prepara los controladores, crea datos iniciales y usuario en sesion.
    def __init__(self):
        self.__conexion = Conexion()
        self.__usuario_controller = UsuarioController(self.__conexion)
        self.__destino_controller = DestinoController(self.__conexion)
        self.__paquete_controller = PaqueteController(self.__conexion)
        self.__reserva_controller = ReservaController(self.__conexion)
        self.__datos_iniciales = self.__usuario_controller.asegurar_datos_iniciales()
        self.__usuario_actual = None

    # Muestra el menu principal de acceso.
    def mostrar_menu(self):
        while True:
            print("\n=== Menú Inicio ===")
            print("1. Iniciar Sesión")
            print("2. Registrar Usuario")
            print("3. Salir")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.iniciar_sesion()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                print("Saliendo del programa...")
                self.__usuario_controller.cerrar_conexion()
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

    # Permite registrar un usuario de rol cliente.
    def registrar_usuario(self):
        try:
            print("\nRegistro de Usuario")
            nombre = input("Nombre: ").strip()
            apellidos = input("Apellidos: ").strip()
            nickname = input("Nickname: ").strip()
            email = input("Email: ").strip()
            telefono = input("Teléfono (incluye código de país sin espacios): ").strip()
            contrasena = pwinput.pwinput("Contraseña: ", mask="*")
            rol_cliente = self.__datos_iniciales["roles"]["cliente"]
            self.__usuario_controller.nuevo_usuario(
                nombre, apellidos, nickname, email, telefono, rol_cliente, contrasena
            )
            input("Usuario registrado exitosamente, presione Enter para continuar...")
        except Exception as error:
            print(f"Error al registrar usuario: {error}")

    # Inicia sesión y redirige al menu segun rolero.
    def iniciar_sesion(self):
        try:
            print("\nInicio de Sesión")
            identificador = input("Email o Nickname: ").strip()
            contrasena = pwinput.pwinput("Contraseña: ", mask="*")
            usuario = self.__usuario_controller.autenticar(identificador, contrasena)
            if not usuario:
                print("Credenciales inválidas, intente nuevamente.")
                return
            self.__usuario_actual = usuario
            print(f"Bienvenido {usuario.nombre}.")
            if usuario.rol_id == self.__datos_iniciales["roles"]["admin"]:
                self.__menu_administrador()
            else:
                self.__menu_cliente()
        except Exception as error:
            print(f"No fue posible iniciar sesión: {error}")

    # Presenta las opciones para administradores.
    def __menu_administrador(self):
        while True:
            print("\n=== Panel Administrador ===")
            print("1. Gestionar destinos")
            print("2. Gestionar paquetes")
            print("3. Revisar reservas")
            print("4. Cerrar Sesión")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.__menu_destinos()
            elif opcion == "2":
                self.__menu_paquetes()
            elif opcion == "3":
                self.__mostrar_reservas_admin()
            elif opcion == "4":
                self.__usuario_actual = None
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    # Presenta las opciones para clientes.
    def __menu_cliente(self):
        while True:
            if self.__usuario_actual is None:
                print("Debe iniciar sesión primero.")
                input("Presione Enter para continuar...")
                return
            print("\n=== Panel Cliente ===")
            print("1. Ver paquetes")
            print("2. Reservar paquete")
            print("3. Ver mis reservas")
            print("4. Ajustes de cuenta")
            print("0. Cerrar Sesión")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.__mostrar_paquetes_disponibles()
            elif opcion == "2":
                self.__crear_reserva_cliente()
            elif opcion == "3":
                self.__mostrar_reservas_cliente()
            elif opcion == "4":
                self.__menu_ajustes_cuenta()
            elif opcion == "0":
                self.__usuario_actual = None
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    # Permite administrar destinos.
    def __menu_destinos(self):
        while True:
            print("\n--- Destinos ---")
            print("1. Crear destino")
            print("2. Listar destinos")
            print("3. Editar destino")
            print("4. Eliminar destino")
            print("5. Volver")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.__crear_destino()
            elif opcion == "2":
                self.__listar_destinos()
            elif opcion == "3":
                self.__editar_destino()
            elif opcion == "4":
                self.__eliminar_destino()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")

    # Permite administrar paquetes.
    def __menu_paquetes(self):
        while True:
            print("\n--- Paquetes Turísticos ---")
            print("1. Crear paquete")
            print("2. Listar paquetes")
            print("3. Cambiar disponibilidad")
            print("4. Eliminar paquete")
            print("5. Volver")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.__crear_paquete()
            elif opcion == "2":
                self.__listar_paquetes()
            elif opcion == "3":
                self.__cambiar_disponibilidad_paquete()
            elif opcion == "4":
                self.__eliminar_paquete()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")

    # Solicita datos y crea un destino.
    def __crear_destino(self):
        try:
            nombre = input("Nombre: ").strip()
            descripcion = input("Descripción: ").strip()
            actividades = input("Actividades (separadas por coma): ").strip()
            costo_base = float(input("Costo base: ").strip())
            self.__destino_controller.crear(nombre, descripcion, actividades, costo_base)
            print("Destino creado correctamente.")
        except Exception as error:
            print(f"No se pudo crear el destino: {error}")

    # Muestra todos los destinos.
    def __listar_destinos(self):
        destinos = self.__destino_controller.listar()
        if not destinos:
            print("No hay destinos registrados.")
            return []
        for destino in destinos:
            print(
                f"[{destino.id}] {destino.nombre} - {destino.descripcion} | Actividades: {destino.actividades} "
                f"| Costo base: {destino.costo_base}"
            )
        return destinos

    # Solicita datos y actualiza un destino.
    def __editar_destino(self):
        try:
            destinos = self.__listar_destinos()
            if not destinos:
                input("Presione Enter para continuar...")
                return
            destino_id = input("ID del destino a editar: ").strip()
            if destino_id == "":
                print("El ID no puede estar vacio")
                return
            if not destino_id.isdigit():
                print("El ID debe ser un número válido.")
                return
            destino_id = int(destino_id)

            destino_obj = self.__destino_controller.obtener(destino_id)
            if not destino_obj:
                print("No se encontró el destino indicado.")
                return

            print("=== Edición de destino ===")
            print("1) Nombre \n2) Descripción \n3) Actividades \n4) Costo base \n5) Cancelar edición")
            select = input("Seleccione el campo a editar (1-5): ").strip()
            if select == "5":
                print("Edición cancelada.")
                input("Presione Enter para continuar...")
                return
            elif select == "1":
                cambio = input("Nuevo nombre: ").strip()
                tipo = "nombre"
            elif select == "2":
                cambio = input("Nueva descripción: ").strip()
                tipo = "descripcion"
            elif select == "3":
                cambio = input("Nuevas actividades: ").strip()
                tipo = "actividades"
            elif select == "4":
                cambio = input("Nuevo costo base: ").strip()
                try:
                    cambio = float(cambio)
                except ValueError:
                    print("El costo base debe ser un número válido.")
                    return
                tipo = "costo_base"
            else:
                print("Opción inválida. Edición cancelada.")
                input("Presione Enter para continuar...")
                return

            actualizado = self.__destino_controller.actualizar(
                destino_id, cambio, tipo
            )
            if actualizado:
                print("Destino actualizado.")
            else:
                print("No se pudo actualizar, verifique el ID.")
        except ValueError as ve:
            print(f"Datos ingresados inválidos: {ve}")        
        except Exception as error:
            print(f"Error al actualizar destino: {error}")

    # Elimina un destino seleccionado.
    def __eliminar_destino(self):
        try:
            destinos = self.__listar_destinos()
            if not destinos:
                input("Presione Enter para continuar...")
                return
            destino_id = input("ID del destino a eliminar: ").strip()
            if destino_id == "" or destino_id.isdigit() is False:
                print("El ID debe ser un número válido.")
                return
            consentimiento = input("¿Está seguro? Esta acción no se puede deshacer s para confirmar, cualquier otra tecla para cancelar: ").strip().lower()
            if consentimiento != "s":
                print("Eliminación cancelada.")
                input("Presione Enter para continuar...")
                return
            eliminado = self.__destino_controller.eliminar(destino_id)
            if eliminado:
                print("Destino eliminado.")
            else:
                print("No se encontró el destino indicado.")
        except Exception as error:
            print(f"Error al eliminar destino: {error}")

    # Solicita datos y crea un paquete turistico.
    def __crear_paquete(self):
        try:
            self.__listar_destinos()
            if not self.__destino_controller.listar():
                input("Presione Enter para continuar...")
                return
            destino_id = input("ID del destino para el paquete: ").strip()
            fecha_inicio = self.__leer_fecha("Fecha inicio (DD-MM-AAAA): ")
            fecha_fin = self.__leer_fecha("Fecha fin (DD-MM-AAAA): ")
            self.__paquete_controller.crear(destino_id, fecha_inicio, fecha_fin, None, True)
            print("Paquete creado correctamente.")
        except Exception as error:
            print(f"No se pudo crear el paquete: {error}")

    # Muestra todos los paquetes.
    def __listar_paquetes(self):
        paquetes = self.__paquete_controller.listar()
        if not paquetes:
            print("No hay paquetes registrados.")
            return
        print("=== Paquetes Turísticos ===")
        for paquete in paquetes:
            print(
                f"[{paquete[0]}] Destino: {paquete[1]} | {paquete[2]} al {paquete[3]} "
                f"| Precio: {paquete[4]} | Disponible: {'Sí' if paquete[5] else 'No'}"
            )

    # Cambia la disponibilidad de un paquete.
    def __cambiar_disponibilidad_paquete(self):
        try:
            paquetes = self.__listar_paquetes()
            if not paquetes:
                input("Presione Enter para continuar...")
                return
            paquete_id = input("ID del paquete: ").strip()
            nuevo_estado = input("¿Marcar como disponible? (s/n): ").strip().lower() == "s"
            actualizado = self.__paquete_controller.actualizar_disponibilidad(paquete_id, nuevo_estado)
            if actualizado:
                print("Disponibilidad actualizada.")
                input("Presione Enter para continuar...")
            else:
                print("No se pudo actualizar, revise el ID.")
                input("Presione Enter para continuar...")
        except Exception as error:
            print(f"Error al cambiar disponibilidad: {error}")

    # Muestra paquetes disponibles segun rango de fechas.
    def __mostrar_paquetes_disponibles(self):
        try:
            # fecha_inicio = self.__leer_fecha("Fecha inicio deseada (DD-MM-AAAA): ")
            # fecha_fin = self.__leer_fecha("Fecha fin deseada (DD-MM-AAAA): ")
            # paquetes = self.__paquete_controller.listar_disponibles(fecha_inicio, fecha_fin)
            paquetes = self.__listar_paquetes()
            #if not paquetes:
               # print("No hay paquetes disponibles para esas fechas.")
                #return
            #for paquete in paquetes:
                #print(
                  #  f"[{paquete[0]}] Destino: {paquete[1]} | {paquete[2]} al {paquete[3]} "
                   # f"| Precio: {paquete[4]}"
              #  )
        except Exception as error:
            print(f"Error al buscar paquetes: {error}")

    # Crea una reserva para el usuario logueado.
    def __crear_reserva_cliente(self):
        if not self.__usuario_actual:
            print("Debe iniciar sesión primero.")
            return
        try:
            self.__mostrar_paquetes_disponibles()
            paquete_id = input("Indique el ID del paquete a reservar: ").strip()
            if paquete_id == "":
                print("El ID no puede estar vacio")
                return
            elif paquete_id.isdigit() is False:
                print("El ID debe ser un número válido.")
                return
            paquete_id = int(paquete_id)
            reserva_id = self.__reserva_controller.crear_reserva(self.__usuario_actual.id, paquete_id)
            if reserva_id:
                print(f"Reserva creada con ID {reserva_id}.")
        except Exception as error:
            print(f"No se pudo crear la reserva: {error}")
        input("Presione Enter para continuar...")

    # Muestra las reservas del usuario logueado.
    def __mostrar_reservas_cliente(self):
        if not self.__usuario_actual:
            print("Debe iniciar sesión primero.")
            return
        reservas = self.__reserva_controller.listar_reservas_usuario(self.__usuario_actual.id)
        if not reservas:
            print("No posee reservas registradas.")
            return
        for reserva in reservas:
            print(
                f"Reserva {reserva[0]} | Paquete {reserva[1]} del {reserva[2]} al {reserva[3]} "
                f"| Precio: {reserva[4]} | Estado: {reserva[5]}"
            )

    # Muestra todas las reservas para el administrador.
    def __mostrar_reservas_admin(self):
        reservas = self.__reserva_controller.listar_todas()
        if not reservas:
            print("No hay reservas registradas.")
            return
        for reserva in reservas:
            print(
                f"Reserva {reserva[0]} | Usuario: {reserva[1]} | Paquete {reserva[2]} "
                f"({reserva[3]} al {reserva[4]}) | Precio: {reserva[5]} | Estado: {reserva[6]}"
            )

    # Lee una fecha en formato AAAA-MM-DD y la valida.
    def __leer_fecha(self, mensaje):
        valor = input(mensaje).strip()
        try:
            fecha = datetime.strptime(valor, "%d-%m-%Y")
            return fecha.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha debe seguir el formato DD-MM-AAAA.")
        
    # Muestra el menu de ajustes de cuenta para el usuario actual.
    def __menu_ajustes_cuenta(self):
        while True:
            if self.__usuario_actual is None:
                return
            print("\n--- Ajustes de Cuenta ---")
            print("1. Cambiar contraseña")
            print("2. Actualizar información personal")
            print("3. Eliminar cuenta")
            print("4. Volver")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.__cambiar_contrasena()
            elif opcion == "2":
                self.__actualizar_informacion_personal()
            elif opcion == "3":
                self.__eliminar_cuenta()
            elif opcion == "4":
                return
            else:
                print("Opción inválida.")

    # Permite al usuario cambiar su contraseña.
    def __cambiar_contrasena(self):
        if not self.__usuario_actual:
            print("Debe iniciar sesión primero.")
            input("Presione Enter para continuar...")
            return

        print("\n=== Cambio de Contraseña ===")
        vieja_contraseña = pwinput.pwinput("Contraseña actual: ", mask="*")
        nueva_contraseña = pwinput.pwinput("Nueva contraseña: ", mask="*")
        try:
            self.__usuario_controller.cambiar_contrasena(
                self.__usuario_actual.id, vieja_contraseña, nueva_contraseña
            )
            print("Contraseña cambiada exitosamente.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as error:
            print(f"No se pudo cambiar la contraseña: {error}")
        input("Presione Enter para continuar...")

    def __actualizar_informacion_personal(self):
        print("=== Tus datos personales ===")
        print(f"1) Nombre: {self.__usuario_actual.nombre}")
        print(f"2) Apellidos: {self.__usuario_actual.apellidos}")
        print(f"3) Nickname: {self.__usuario_actual.nickname}")
        print(f"4) Email: {self.__usuario_actual.email}")
        print(f"5) Teléfono: {self.__usuario_actual.telefono}")
        print("0) Salir")
        opcion = input("Seleccione el campo a modificar: ").strip()

        campos = { 
            "1": "nombre",
            "2": "apellidos",
            "3": "nickname",
            "4": "email",
            "5": "telefono"
        }

        if opcion in campos:
            nuevo_valor = input(f"Ingrese el nuevo valor para {campos[opcion]}: ").strip()
            try:
                self.__usuario_controller.modificar_usuario(
                    self.__usuario_actual.id, campos[opcion], nuevo_valor
                )
                print(f"{campos[opcion].capitalize()} actualizado correctamente.")
            except Exception as ValueError:
                print(f"Error: {ValueError}")
            except Exception as error:
                print(f"Error al actualizar {campos[opcion]}: {error}")
        input("Presione Enter para continuar...")

    def __eliminar_cuenta(self):
        print("=== Eliminar Cuenta ===")
        confirmacion = input("¿Está seguro de que desea eliminar su cuenta? Esta acción no se puede deshacer (s/n): ").strip().lower()
        if confirmacion == "s":
            try:
                self.__usuario_controller.eliminar_usuario(self.__usuario_actual.id)
                print("Cuenta eliminada exitosamente.")
                self.__usuario_actual = None
            except Exception as error:
                print(f"No se pudo eliminar la cuenta: {error}")
        else:
            print("Eliminación de cuenta cancelada.")
        input("Presione Enter para continuar...")

    def __eliminar_paquete(self):
        try:
            paquetes = self.__paquete_controller.listar()
            if not paquetes:
                print("No hay paquetes disponibles para eliminar.")
                input("Presione Enter para continuar...")
                return
            print("=== Paquetes Turísticos ===")
            for paquete in paquetes:
                print(
                    f"[{paquete[0]}] Destino: {paquete[1]} | {paquete[2]} al {paquete[3]} "
                    f"| Precio: {paquete[4]} | Disponible: {'Sí' if paquete[5] else 'No'}"
                )
            paquete_id = input("ID del paquete a eliminar: ").strip()
            if paquete_id == "" or not paquete_id.isdigit():
                print("El ID debe ser un número válido.")
                input("Presione Enter para continuar...")
                return
            consentimiento = input("¿Está seguro? Esta acción no se puede deshacer (s/n): ").strip().lower()
            if consentimiento != "s":
                print("Eliminación cancelada.")
                input("Presione Enter para continuar...")
                return
            eliminado = self.__paquete_controller.eliminar(paquete_id)
            if eliminado:
                print("Paquete eliminado.")
            else:
                print("No se encontró el paquete indicado.")
        except Exception as error:
            print(f"Error al eliminar paquete: {error}")
        input("Presione Enter para continuar...")
