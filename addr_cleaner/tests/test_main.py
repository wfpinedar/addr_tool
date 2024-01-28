# tests/test_main.py

import pytest
from addr_cleaner.addr_cleaner.gui.limpiador.LimpiadorApp import estandarizar_direccion

def test_estandarizar_direccion():
    assert estandarizar_direccion("Cl 123") == "Calle 123"
    assert estandarizar_direccion("Cr 456") == "Carrera 456"
    assert estandarizar_direccion("Av 789") == "Avenida 789"
    # Agrega más tests según las reglas de estandarización que tengas

def test_limpiar_archivo(tmpdir):
    # Crear un DataFrame de prueba y guardarlo como un archivo Excel
    df_prueba = pd.DataFrame({"direccion": ["Cl 123", "Cr 456", "Av 789"],
                              "ciudad": ["Bogotá", "Medellín", "Cali"]})
    archivo_prueba = tmpdir.join("prueba.xlsx")
    df_prueba.to_excel(archivo_prueba)

    # Ejecutar la función de limpieza en el archivo de prueba
    archivo_salida = tmpdir.join("salida.xlsx")
    divipola_dict = {'Bogotá': '11001', 'Medellín': '05001', 'Cali': '76001'}
    limpiar_archivo(archivo_prueba, archivo_salida, "direccion", divipola_dict)

    # Leer el archivo de salida y verificar las correcciones
    df_resultado = pd.read_excel(archivo_salida)
    assert df_resultado["direccion_estandarizada"].equals(df_prueba["direccion"].apply(estandarizar_direccion))
