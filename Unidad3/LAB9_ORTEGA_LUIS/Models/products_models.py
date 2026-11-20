from Controller.conection_db import Database_connection


class Product:
    def __init__(self, nombre="", precio=0, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.db = Database_connection()

    def get_all(self):
        query = """
            SELECT id_product, nombre, precio, stock
            FROM products
            ORDER BY id_product
        """

        return self.db.ejecutar_consulta(query)

    def save(self):
        query = """
            INSERT INTO products (nombre, precio, stock)
            VALUES (%s, %s, %s)
        """

        datos = (self.nombre, self.precio, self.stock)

        return self.db.ejecutar_cambio(query, datos)
