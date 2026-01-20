from geocoder_api.db import DEFAULT_DB_PATH, ensure_db


if __name__ == "__main__":
    path = ensure_db(DEFAULT_DB_PATH)
    print(f"Base de datos creada y poblada en {path}")
