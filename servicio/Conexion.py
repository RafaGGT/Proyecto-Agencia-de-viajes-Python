import mysql.connector

class Conexion:
    def __init__(self, user="root", password= "root", database = "bdagencia", host = "localhost", port = 3306):
        self.conexion = mysql.connector.connect(
            user = user,
            password = password,
            database = database,
            host = host,
            port = port
        )

    def obtener_conexion(self):
        return self.conexion

    def cerrar_conexion(self):
        self.conexion.close()