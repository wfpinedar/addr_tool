from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Función para obtener coordenadas de la base de datos
def obtener_coordenadas(direccion: str):
    conn = sqlite3.connect('.db')
    cursor = conn.cursor()
    cursor.execute("SELECT latitud, longitud FROM geocoding WHERE direccion = ?", (direccion,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

@app.get("/geocodificar/")
async def geocodificar(direccion: str):
    coordenadas = obtener_coordenadas(direccion)
    if coordenadas:
        return {"latitud": coordenadas[0], "longitud": coordenadas[1]}
    else:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
