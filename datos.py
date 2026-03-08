import json
import os

NOMBRE_ARCHIVO = "productos.json"

def guardar_datos(inventario: list):
    """
    Toma la lista de diccionarios y la vuelca en un archivo físico.
    Usa 'indent=4' para que el archivo sea legible por humanos.
    """
    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(inventario, f, indent=4, ensure_ascii=False)
        print("✅ Datos guardados correctamente.")
    except Exception as e:
        print(f"❌ Error al guardar en el disco: {e}")

def cargar_datos() -> list:
    """
    Lee el archivo JSON. Si no existe, devuelve una lista vacía 
    para que el programa no "explote" al iniciar.
    """
    # Verificamos si el archivo existe antes de intentar abrirlo
    if not os.path.exists(NOMBRE_ARCHIVO):
        return []

    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Si el archivo está corrupto o vacío, devolvemos lista vacía
        return []
    except Exception as e:
        print(f"❌ Error inesperado al cargar datos: {e}")
        return []