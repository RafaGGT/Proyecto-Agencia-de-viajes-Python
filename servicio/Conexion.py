import mysql.connector

class Conexion:
    # Crea una conexion manejada a la base de datos MySQL usando los parametros de acceso.
    def __init__(self, user="viajes_admin", password="123", database="bdagencia", host="localhost", port=3306):
        try:
            self.conexion = mysql.connector.connect(
                user=user,
                password=password,
                database=database,
                host=host,
                port=port,
                autocommit=False,
            )
        except mysql.connector.Error as error:
            raise ConnectionError(f"No fue posible conectar con la base de datos: {error}")

    # Retorna la conexion activa para reutilizarla en los servicios.
    def obtener_conexion(self):
        return self.conexion

    # Cierra la conexion abierta de manera segura.
    def cerrar_conexion(self):
        try:
            self.conexion.close()
        except mysql.connector.Error:
            pass
