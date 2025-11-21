from datetime import datetime

class ReservaService:
    # Inicia el servicio con la conexion compartida.
    def __init__(self, conexion):
        self.__conexion = conexion.obtener_conexion()

    # Crea los estados basicos de las reservas y devuelve sus ids.
    def asegurar_estados(self):
        estados = ["pendiente", "confirmada", "cancelada"]
        resultado = {}
        for estado in estados:
            resultado[estado] = self.__crear_estado_si_no_existe(estado)
        return resultado

    # Genera una nueva reserva con el estado indicado.
    def crear_reserva(self, usuario_id, paquete_id, estado_id):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                INSERT INTO reservas (usuario_id, paquete_id, estado_id, fecha_reserva)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(
                consulta,
                (usuario_id, paquete_id, estado_id, datetime.now()),
            )
            self.__conexion.commit()
            return cursor.lastrowid
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    # Lista las reservas de un usuario concreto.
    def listar_reservas_usuario(self, usuario_id):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                SELECT r.id, p.id, p.fecha_inicio, p.fecha_fin, p.precio_total, e.nombre
                FROM reservas r
                INNER JOIN paquetes_turisticos p ON p.id = r.paquete_id
                INNER JOIN estado e ON e.id = r.estado_id
                WHERE r.usuario_id=%s;
            """
            cursor.execute(consulta, (usuario_id,))
            return cursor.fetchall()
        except Exception:
            return []
        finally:
            cursor.close()

    # Lista todas las reservas existentes para administracion.
    def listar_todas(self):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                SELECT r.id, u.email, p.id, p.fecha_inicio, p.fecha_fin, p.precio_total, e.nombre
                FROM reservas r
                INNER JOIN usuarios u ON u.id = r.usuario_id
                INNER JOIN paquetes_turisticos p ON p.id = r.paquete_id
                INNER JOIN estado e ON e.id = r.estado_id;
            """
            cursor.execute(consulta)
            return cursor.fetchall()
        except Exception:
            return []
        finally:
            cursor.close()

    # Crea el estado solicitado si no existe.
    def __crear_estado_si_no_existe(self, nombre_estado):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute("SELECT id FROM estado WHERE nombre=%s LIMIT 1;", (nombre_estado,))
            fila = cursor.fetchone()
            if fila:
                return fila[0]
            cursor.execute("INSERT INTO estado (nombre) VALUES (%s);", (nombre_estado,))
            self.__conexion.commit()
            return cursor.lastrowid
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()
