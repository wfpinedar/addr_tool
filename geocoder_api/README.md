# API de Geocodificación

## Descripción
Esta API de geocodificación proporciona un servicio para convertir direcciones en coordenadas geográficas (latitud y longitud). Basada en FastAPI y SQLite, permite a los usuarios consultar direcciones almacenadas en una base de datos y recibir sus coordenadas correspondientes.

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Configuración del Entorno
Se recomienda usar un entorno virtual para instalar las dependencias. Para crear y activar un entorno virtual, ejecute:

```bash
python -m venv venv
source venv/bin/activate  # En Windows use `venv\Scripts\activate`
```

### Instalación de Dependencias
Este proyecto utiliza Poetry para la gestión de dependencias. Instale Poetry y luego las dependencias del proyecto:

```bash
pip install poetry
poetry install
```
### Configuración de la Base de Datos
Antes de ejecutar la API, es necesario crear y poblar la base de datos SQLite. Ejecute el siguiente script para hacerlo:

```bash
python geocoder_api/crear_db.py
```

Asegúrese de tener el archivo CSV con los datos de geocodificación en la ruta correcta.

### Ejecución de la API

Para iniciar el servidor de la API, ejecute:

```
poetry run uvicorn main:app --reload
```

La API estará disponible en http://127.0.0.1:8000.

### Uso de la API

Para geocodificar una dirección, realice una solicitud GET a /geocodificar/ con el parámetro de dirección. Por ejemplo:

```
http://127.0.0.1:8000/geocodificar/?direccion=Tu+Direccion
```

O en su defecto ir a la ruta http://127.0.0.1:8000/docs en donde fastAPI dispone una documentación interactiva hecha con swagger. 
