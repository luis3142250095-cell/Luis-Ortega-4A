import csv
import json
from fpdf import FPDF


class Exportador:
    def exportar(self, datos, ruta_archivo):
        raise NotImplementedError(
            "Este metodo debe ser implementado por la subclase.")

    def preparar_datos(self, datos):
        return [
            {
                "id_product": int(p["id_product"]),
                "nombre": str(p["nombre"]),
                "precio": float(p["precio"]),
                "stock": int(p["stock"])
            }
            for p in datos
        ]


class ExportadorCSV(Exportador):
    def exportar(self, datos, ruta_archivo):
        productos = self.preparar_datos(datos)
        with open(ruta_archivo, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.DictWriter(
                archivo,
                fieldnames=["id_product", "nombre", "precio", "stock"]
            )
            escritor.writeheader()
            escritor.writerows(productos)
        return ruta_archivo


class ExportadorTXT(Exportador):
    def exportar(self, datos, ruta_archivo):
        productos = self.preparar_datos(datos)
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("--- REPORTE DE PRODUCTOS ---\n")
            for p in productos:
                archivo.write(
                    f'ID: {p["id_product"]} | '
                    f'Nombre: {p["nombre"]} | '
                    f'Precio: ${p["precio"]:.2f} | '
                    f'Stock: {p["stock"]}\n'
                )
        return ruta_archivo


class ExportadorJSON(Exportador):
    def exportar(self, datos, ruta_archivo):
        productos = self.preparar_datos(datos)
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, ensure_ascii=False, indent=4)
        return ruta_archivo


class ExportadorPDF(Exportador):
    def exportar(self, datos, ruta_archivo):
        productos = self.preparar_datos(datos)
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Reporte de Inventario de Productos", ln=1, align="C")
        pdf.ln(6)
        pdf.set_font("Arial", "B", 10)
        for titulo, ancho in [("ID", 18), ("Nombre", 95), ("Precio", 35), ("Stock", 32)]:
            pdf.cell(ancho, 9, titulo, border=1)
        pdf.ln(9)
        pdf.set_font("Arial", size=9)
        for p in productos:
            nombre = p["nombre"][:38]
            nombre = nombre.encode(
                "latin-1", errors="replace").decode("latin-1")
            pdf.cell(18, 8, str(p["id_product"]), border=1)
            pdf.cell(95, 8, nombre, border=1)
            pdf.cell(35, 8, f'${p["precio"]:.2f}', border=1)
            pdf.cell(32, 8, str(p["stock"]), border=1)
            pdf.ln(8)
        pdf.output(ruta_archivo)
        return ruta_archivo
