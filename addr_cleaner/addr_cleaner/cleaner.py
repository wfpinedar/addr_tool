import re
import pandas as pd
from joblib import load

# Cargar el modelo
modelo_cargado = load('./addr_cleaner/modelo_direccion.joblib')


def estandarizar_direccion(direccion):
    if pd.isna(direccion):
        return direccion
    direccion = re.sub(r'\bCL\b', 'Calle', direccion)
    direccion = re.sub(r'\bCR\b', 'Carrera', direccion)
    direccion = re.sub(r'\bAV\b', 'Avenida', direccion)
    direccion = re.sub(r'\b#\b', 'No', direccion)
    return direccion.strip()

def estandarizar_direccion_modelo(direccion):
    if pd.isna(direccion):
        return direccion
    direccion_estandarizada = modelo_cargado.predict([direccion])[0]
    print(direccion_estandarizada)
    return str(direccion_estandarizada)  

def limpiar_archivo(ruta_entrada, ruta_salida, columna_direccion, divipola_dict):
    df = pd.read_excel(ruta_entrada)

    if columna_direccion not in df.columns:
        raise ValueError(f"La columna '{columna_direccion}' no se encuentra en el archivo.")

    df['direccion_estandarizada'] = df[columna_direccion].apply(estandarizar_direccion)
    df['direccion_estandarizada_modelo'] = df[columna_direccion].apply(estandarizar_direccion_modelo)
    # df['codigo_ciudad'] = df['ciudad'].map(divipola_dict) # TODO: divipola_dict acorde con los codigos de ciudad
    df.to_excel(ruta_salida, index=False)