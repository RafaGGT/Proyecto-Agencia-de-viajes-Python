from modelo.Destino import Destino

class DestinoService:
    # Inicializa el servicio de destinos con la conexion compartida.
    def __init__(self, conexion):
        self.__conexion = conexion.obtener_conexion()

    # Inserta un destino y devuelve el id generado.
    def crear_destino(self, destino):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                INSERT INTO destinos (nombre, descripcion, actividades, costo_base)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(
                consulta,
                (
                    destino.nombre,
                    destino.descripcion,
                    destino.actividades,
                    destino.costo_base,
                ),
            )
            self.__conexion.commit()
            return cursor.lastrowid
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    # Obtiene todos los destinos registrados.
    def listar_destinos(self):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute("SELECT id, nombre, descripcion, actividades, costo_base FROM destinos;")
            filas = cursor.fetchall()
            return [
                Destino(
                    id=fila[0],
                    nombre=fila[1],
                    descripcion=fila[2],
                    actividades=fila[3],
                    costo_base=fila[4],
                )
                for fila in filas
            ]
        except Exception:
            return []
        finally:
            cursor.close()

    # Recupera un destino especifico por id.
    def obtener_destino(self, destino_id):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute(
                "SELECT id, nombre, descripcion, actividades, costo_base FROM destinos WHERE id=%s;",
                (destino_id,),
            )
            fila = cursor.fetchone()
            if not fila:
                return None
            return Destino(
                id=fila[0],
                nombre=fila[1],
                descripcion=fila[2],
                actividades=fila[3],
                costo_base=fila[4],
            )
        except Exception:
            return None
        finally:
            cursor.close()

    # Actualiza los campos de un destino existente.
    def actualizar_destino(self, destino_id, destino_actualizado):
        cursor = self.__conexion.cursor()
        try:
            consulta = """
                UPDATE destinos
                SET nombre=%s, descripcion=%s, actividades=%s, costo_base=%s
                WHERE id=%s;
            """
            cursor.execute(
                consulta,
                (
                    destino_actualizado.nombre,
                    destino_actualizado.descripcion,
                    destino_actualizado.actividades,
                    destino_actualizado.costo_base,
                    destino_id,
                ),
            )
            self.__conexion.commit()
            return cursor.rowcount > 0
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()

    # Elimina un destino por su identificador.
    def eliminar_destino(self, destino_id):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute("DELETE FROM destinos WHERE id=%s;", (destino_id,))
            self.__conexion.commit()
            return cursor.rowcount > 0
        except Exception as error:
            self.__conexion.rollback()
            raise error
        finally:
            cursor.close()
