# addr_tool — herramientas de geocodificación y limpieza de direcciones

Repo con utilidades GIS: una API de geocodificación rápida (FastAPI + SQLite) y un módulo de limpieza/estandarización de direcciones con modelo ML ligero.

## Ejecutar la API en 1 comando
```bash
docker compose up --build
```
- API: http://localhost:8000
- Docs OpenAPI: http://localhost:8000/docs

### Ejemplo cURL
```bash
curl "http://localhost:8000/geocode?direccion=KM%207%20AUTOPISTA%20FLORIDABLANCA"
```
Respuesta:
```json
{
  "direccion": "KM 7 AUTOPISTA FLORIDABLANCA",
  "latitud": 7.08524,
  "longitud": -73.10344
}
```

## Estructura
- `geocoder_api/`: API FastAPI con BD SQLite semilla (`db_xample.csv`) y tests (`pytest`).
- `addr_cleaner/`: módulo GUI/CLI para estandarizar direcciones con un modelo entrenado (`modelo_direccion.joblib`).
- `addr_model/`: (placeholder) espacio para experimentos de modelado adicional.

Cada carpeta tiene su README para instalación detallada. El `docker-compose.yml` levanta la API geocodificadora directamente.

## Stack destacado
- GIS/geocoding: normalización de direcciones y lookup determinístico en SQLite (ampliable a tu propio dataset).
- FastAPI + Uvicorn + OpenAPI para la API.
- Pandas para ingestión y normalización de CSV/Excel.
- Pytest para smoke tests de la API.
