import importlib
import os
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


def get_client(tmp_path: Path):
    # Forzamos DB en tmp para que no dependa del host
    db_path = tmp_path / "geocoding.db"
    os.environ["DB_PATH"] = str(db_path)
    sys.path.append(str(Path(__file__).resolve().parents[1]))
    module = importlib.import_module("main")
    module = importlib.reload(module)
    return TestClient(module.app)


def test_geocode_hit(tmp_path):
    client = get_client(tmp_path)
    with client:
        resp = client.get("/geocode", params={"direccion": "km 7 autopista floridablanca"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["direccion"].upper().startswith("KM 7 AUTOPISTA")
        assert data["latitud"] == pytest.approx(7.08524, rel=1e-4)
        assert data["longitud"] == pytest.approx(-73.10344, rel=1e-4)


def test_geocode_not_found(tmp_path):
    client = get_client(tmp_path)
    with client:
        resp = client.get("/geocode", params={"direccion": "direccion inexistente 123"})
        assert resp.status_code == 404
        assert resp.json()["detail"] == "Direccion no encontrada"
