from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from geocoder_api.db import DEFAULT_DB_PATH, ensure_db, fetch_coordinates


class GeocodeResult(BaseModel):
    direccion: str
    latitud: float
    longitud: float


app = FastAPI(
    title="Addr Tool Geocoder API",
    description=(
        "Servicio rapido para geocodificar direcciones colombianas "
        "a partir de un dataset semilla local (extensible con tu propia BD)."
    ),
    version="0.2.0",
)


@app.on_event("startup")
def _startup():
    ensure_db(DEFAULT_DB_PATH)


@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok", "db_path": str(Path(DEFAULT_DB_PATH).resolve())}


@app.get(
    "/geocode",
    response_model=GeocodeResult,
    tags=["geocoding"],
    summary="Geocodifica una direccion",
)
def geocode(direccion: str = Query(..., description="Direccion libre a buscar")):
    row = fetch_coordinates(direccion, DEFAULT_DB_PATH)
    if not row:
        raise HTTPException(status_code=404, detail="Direccion no encontrada")
    direccion_db, lat, lon = row
    return GeocodeResult(direccion=direccion_db, latitud=lat, longitud=lon)
