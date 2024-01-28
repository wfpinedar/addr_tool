import sqlite3
import pandas as pd
# Leer el archivo CSV en un DataFrame
df = pd.read_csv('./geocoder_api/db_xample.csv', sep=';')

# Conectar a la base de datos SQLite (se crea si no existe)
conn = sqlite3.connect('.db')
cursor = conn.cursor()

# Crear tabla en la base de datos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS geocoding (
        id INTEGER PRIMARY KEY,
        direccion TEXT,
        latitud REAL,
        longitud REAL
    )
''')

# Insertar datos del DataFrame en la tabla
df.to_sql('geocoding', conn, if_exists='replace', index=False)

# Cerrar la conexión a la base de datos
conn.close()
print("Base de datos creada y poblada con éxito.")