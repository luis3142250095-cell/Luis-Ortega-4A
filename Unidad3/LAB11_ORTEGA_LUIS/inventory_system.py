

class ErrorInventario(Exception):
    pass


class ProductoNoEncontradoError(ErrorInventario):
    pass


class CantidadInvalida(ErrorInventario):
    pass


class StockInsuficienteError(ErrorInventario):
    pass

# clase Product


class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise CantidadInvalida("La cantidad debe ser mayor a cero.")
        else:
            if cantidad > self.stock:
                raise StockInsuficienteError(
                    "Stock insuficiente para retirar la cantidad solicitada.")
        self.stock -= cantidad


class Inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01", 10),
            "P02": Producto("P02", 5),
            "P03": Producto("P03", 8),
            "P04": Producto("P04", 15)
        }

    def retirar_producto(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontradoError("Producto no encontrado.")
        self.productos[codigo].retirar(cantidad)


def main():
    inventario = Inventario()
    codigo_producto = input("Ingrese el código del producto a retirar: ")
    try:
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        inventario.retirar_producto(codigo_producto, cantidad)
        print(
            f"Se han retirado {cantidad} unidades del producto {codigo_producto}.")
    except ValueError:
        print("La cantidad debe ser un número entero.")
    except ProductoNoEncontradoError as error:
        print(f"No se pudo retirar el producto: {error}")
    except CantidadInvalida as error:
        print(f"Error en la cantidad: {error}")
    except StockInsuficienteError as error:
        print(f"Error en el stock: {error}")


if __name__ == "__main__":
    main()
