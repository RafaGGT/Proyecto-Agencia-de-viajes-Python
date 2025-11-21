from datetime import datetime
from modelo.PaqueteTuristico import PaqueteTuristico

class PaqueteService:
    # Inicia el servicio de paquetes con la conexion compartida.
    def __init__(self, conexion):
        self.__conexion = conexion.obtener_conexion()

    # Crea un paquete turistico calculando el precio si no viene definido.
    def crear_paquete(self, paquete, costo_base_destino=0):
        cursor = self.__conexion.cursor()
        try:
            precio = paquete.precio_total
            if precio is None or precio == 0:
                precio = self.__calcular_precio_total(paquete, costo_base_destino)

            consulta = """
                INSERT INTO paquetes_turisticos (destino_id, fecha_inicio, fecha_fin, precio_total, disponible)
                VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(
                consulta,
                (
                    paquete.destino_id,
                    paquete.fecha_inicio,
                    paquete.fecha_fin,
                    precio,
                    paquete.disponible,
                ),
            )
            self.__conexion.commit()
            return cursor.lastrowid
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    # Lista todos los paquetes creados junto al destino.
    def listar_paquetes(self):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                SELECT p.id, d.nombre, p.fecha_inicio, p.fecha_fin, p.precio_total, p.disponible, p.destino_id
                FROM paquetes_turisticos p
                INNER JOIN destinos d ON d.id = p.destino_id;
            """
            cursor.execute(consulta)
            return cursor.fetchall()
        except Exception:
            return []
        finally:
            cursor.close()

    # Filtra los paquetes disponibles que cubren el rango de fechas solicitado.
    def listar_disponibles_por_fecha(self, fecha_inicio, fecha_fin):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                SELECT p.id, d.nombre, p.fecha_inicio, p.fecha_fin, p.precio_total, p.disponible, p.destino_id
                FROM paquetes_turisticos p
                INNER JOIN destinos d ON d.id = p.destino_id
                WHERE p.disponible = TRUE
                  AND p.fecha_inicio <= %s
                  AND p.fecha_fin >= %s;
            """
            cursor.execute(consulta, (fecha_inicio, fecha_fin))
            return cursor.fetchall()
        except Exception:
            return []
        finally:
            cursor.close()

    # Actualiza la disponibilidad del paquete.
    def actualizar_disponibilidad(self, paquete_id, disponible):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute(
                "UPDATE paquetes_turisticos SET disponible=%s WHERE id=%s;",
                (disponible, paquete_id),
            )
            self.__conexion.commit()
            return cursor.rowcount > 0
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    # Recupera un paquete especifico.
    def obtener_paquete(self, paquete_id):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute(
                """
                SELECT id, destino_id, fecha_inicio, fecha_fin, precio_total, disponible
                FROM paquetes_turisticos
                WHERE id=%s;
                """,
                (paquete_id,),
            )
            fila = cursor.fetchone()
            if not fila:
                return None
            return PaqueteTuristico(
                id=fila[0],
                destino_id=fila[1],
                fecha_inicio=fila[2],
                fecha_fin=fila[3],
                precio_total=fila[4],
                disponible=fila[5],
            )
        except Exception:
            return None
        finally:
            cursor.close()

    # Calcula el precio total tomando la duracion del viaje.
    def __calcular_precio_total(self, paquete, costo_base_destino):
        try:
            fecha_inicio = self.__parsear_fecha(paquete.fecha_inicio)
            fecha_fin = self.__parsear_fecha(paquete.fecha_fin)
            duracion = (fecha_fin - fecha_inicio).days or 1
            return float(costo_base_destino) * float(duracion)
        except Exception:
            return costo_base_destino

    # Convierte fechas en cadena a objetos datetime para calculos.
    def __parsear_fecha(self, fecha_valor):
        if isinstance(fecha_valor, datetime):
            return fecha_valor
        return datetime.strptime(str(fecha_valor), "%Y-%m-%d")
