# API de Geocodificación (FastAPI)

Servicio ligero para geocodificar direcciones (ejemplo Colombia) usando una BD SQLite precargada con un dataset semilla. Incluye Docker, OpenAPI y tests básicos.

## Levantar en 1 comando (Docker)
```bash
docker compose up --build
```
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

## Levantar local (sin Docker)
```bash
cd geocoder_api
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python geocoder_api/crear_db.py   # prepara la BD con el CSV semilla
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Variables de entorno:
- `DB_PATH` (opcional): ruta al SQLite que quieras usar. Por defecto `geocoder_api/data/geocoding.db`.

## Ejemplos de uso
### cURL
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

### OpenAPI interactivo
1. Abre http://localhost:8000/docs
2. El endpoint `GET /geocode` acepta el query param `direccion`.
3. Respuestas esperadas:
   - `200`: payload con `direccion`, `latitud`, `longitud`.
   - `404`: `{"detail": "Direccion no encontrada"}`.

## Tests
```bash
cd geocoder_api
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Notas GIS
- Normaliza direcciones a mayúsculas y espacios simples para coincidencia determinística.
- La BD se autogenera con el CSV semilla (`geocoder_api/db_xample.csv`), pero puedes reemplazarlo/crear tu propia BD apuntando `DB_PATH` a otra ruta y precargando tus datos.
