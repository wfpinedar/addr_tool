# Paquete addr_model
En este se ha realizado un entrenamiento extremadamente basico de lo que seria el entrenamiento de un modelo. 

## Instalación

Es necesario tener python 3.9 o superior y poetry instalados

```bash
poetry install
```

## Ejecución
En el fichero main.py reemplazar la ruta del archivo excel que servira como insumo para el entrenamiento y las columnas DIRECCION y direccion_estandarizada por las que tenga el nuevo archivo. 

Despues correr el comando:

```bash
poetry run python main.py
```

El modelo entrenado quedara guardado en el archivo _modelo_direccion.joblib_.
