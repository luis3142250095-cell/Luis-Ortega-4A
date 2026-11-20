import mysql.connector
from mysql.connector import Error
from Controller.config import DB_config


class Database_connection:
    def __init__(self):
        self.config = DB_config

    def get_connection(self):
        try:
            return mysql.connector.connect(**self.config)

        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.get_connection()

        if conexion is None:
            return None

        cursor = None

        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchall()

        except Error as e:
            print(f"Error en la consulta: {e}")
            return None

        finally:
            if cursor is not None:
                cursor.close()

            conexion.close()

    def ejecutar_cambio(self, query, params=()):
        conexion = self.get_connection()

        if conexion is None:
            return False

        cursor = None

        try:
            cursor = conexion.cursor()
            cursor.execute(query, params)

            conexion.commit()
            return True

        except Error as e:
            conexion.rollback()
            print(f"Error al guardar: {e}")
            return False

        finally:
            if cursor is not None:
                cursor.close()

            conexion.close()
