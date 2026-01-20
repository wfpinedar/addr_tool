import os
import re
import sqlite3
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd


# Ruta de la base de datos (puede sobreescribirse con la variable de entorno DB_PATH)
DEFAULT_DB_PATH = Path(
    os.getenv(
        "DB_PATH",
        Path(__file__).resolve().parent / "data" / "geocoding.db",
    )
)

# Ruta al dataset semilla con puntos de ejemplo
CSV_PATH = Path(__file__).resolve().parent / "db_xample.csv"


def normalize_address(address: str) -> str:
    cleaned = re.sub(r"\s+", " ", address or "").strip()
    return cleaned.upper()


def ensure_db(db_path: Path = DEFAULT_DB_PATH, csv_path: Path = CSV_PATH) -> Path:
    """
    Crea la base de datos y la carga con el CSV de ejemplo si está vacía.
    Devuelve la ruta final de la base.
    """
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS geocoding (
            direccion TEXT PRIMARY KEY,
            direccion_normalizada TEXT NOT NULL,
            latitud REAL NOT NULL,
            longitud REAL NOT NULL
        )
        """
    )
    existing = cursor.execute("SELECT COUNT(*) FROM geocoding").fetchone()[0]
    if existing == 0:
        df = pd.read_csv(csv_path, sep=";", decimal=",", encoding="utf-8-sig")
        df["direccion_normalizada"] = df["direccion"].apply(normalize_address)
        df = df[["direccion", "direccion_normalizada", "latitud", "longitud"]]
        df.to_sql("geocoding", conn, if_exists="replace", index=False)
        cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_geocoding_norm ON geocoding(direccion_normalizada)"
        )
        conn.commit()
    conn.close()
    return db_path


def fetch_coordinates(address: str, db_path: Path = DEFAULT_DB_PATH) -> Optional[Tuple[str, float, float]]:
    normalized = normalize_address(address)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT direccion, latitud, longitud FROM geocoding WHERE direccion_normalizada = ?",
        (normalized,),
    )
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    return row[0], float(row[1]), float(row[2])
