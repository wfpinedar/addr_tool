# Nombre del Proyecto

Descripción breve del proyecto.

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

### Ejecución del programa

para ejecutar este programa puede usar el siguiente comando: 

```
poetry run python addr_cleaner/gui.py
```

este abre una interfaz grafica en la cual debe cargar el archivo de excel y este leera las columnas y debe seleccionar la columna que quiere limpiar.
