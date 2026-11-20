from Models.products_models import Product
from Models.exporters import (
    ExportadorCSV, ExportadorTXT, ExportadorJSON, ExportadorPDF
)


class ExportController:
    def __init__(self):
        self.modelo = Product()
        self.exportadores = {
            "CSV": ExportadorCSV,
            "TXT": ExportadorTXT,
            "JSON": ExportadorJSON,
            "PDF": ExportadorPDF
        }

    def generar_reporte(self, formato, ruta_archivo):
        productos = self.modelo.get_all()
        if productos is None:
            raise ConnectionError(
                "No se pudo consultar la base de datos MySQL.")
        if not productos:
            raise ValueError("No hay productos registrados para exportar.")
        clase_exportadora = self.exportadores.get(formato)
        if clase_exportadora is None:
            raise ValueError("Selecciona un formato de exportacion valido.")
        exportador = clase_exportadora()
        return exportador.exportar(productos, ruta_archivo)
