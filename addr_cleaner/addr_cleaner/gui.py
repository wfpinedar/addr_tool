import flet as ft
import pandas as pd
import re
from cleaner import limpiar_archivo, estandarizar_direccion
import os

def cargar_columnas(selection):
    try:
        df = pd.read_excel(selection)
        return df.columns.tolist()
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")


def main(page: ft.Page):
    # Elementos de la interfaz
    # ruta_input = ft.TextField(label="Ruta del archivo CSV")
    # columna_input = ft.TextField(label="Nombre de la columna de direcciones: ")
    limpiar_btn = ft.ElevatedButton("Limpiar Archivo")
    close_btn = ft.ElevatedButton("Cerrar", on_click=lambda _: page.window_close())
    resultado_txt = ft.Text()
    doc_columns = ft.Dropdown(
        label="Nombre de la columna de direcciones: ",
        width=300,
        options=[
            ],
    )

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        file_path = ",".join(map(lambda f: f.path, e.files))
        for col in cargar_columnas(file_path):
            doc_columns.options.append(ft.dropdown.Option(col))
        doc_columns.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    

    page.overlay.append(pick_files_dialog)

    file_selector = ft.Row(
            [
                ft.ElevatedButton(
                    "Seleccione archivo",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False,
                        allowed_extensions = ["xls", "xlsx"]
                    ),
                ),
                selected_files,
            ]
        )

    
    # Función que se ejecuta al hacer clic en el botón
    def limpiar_click(e):
        try:
            divipola_dict = {'Bogotá': '11001', 'Medellín': '05001'}
            archivo_salida = os.path.join(os.path.dirname(selected_files.value), 'out2.xlsx')
            limpiar_archivo(selected_files.value, archivo_salida, doc_columns.value, divipola_dict)
            resultado_txt.value = f"Archivo limpiado con éxito en: {archivo_salida}"
            resultado_txt.update()
        except Exception as ex:
            print(ex)
            resultado_txt.value = f"Error: {ex}"
            resultado_txt.update()

    limpiar_btn.on_click = limpiar_click

    page.add(file_selector, doc_columns, limpiar_btn, close_btn,resultado_txt)
    limpiar_btn.update()

if __name__ == "__main__":
    ft.app(target=main)
