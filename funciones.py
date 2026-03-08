"""
Módulo de lógica de negocio para el sistema de inventario.
Contiene las funciones para manipular la lista de productos.
"""

def agregar_producto(inventario: list, nombre: str, cantidad: int, precio: float) -> list:
    """
    Crea un nuevo producto y lo añade a la lista existente.
    
    Args:
        inventario (list): Lista actual de productos (diccionarios).
        nombre (str): Nombre del producto.
        cantidad (int): Stock disponible.
        precio (float): Precio unitario.
        
    Returns:
        list: El inventario actualizado.
    """
    nuevo_item = {
        "nombre": nombre.capitalize(),
        "cantidad": cantidad,
        "precio": precio
    }
    inventario.append(nuevo_item)
    return inventario

def buscar_bajo_stock(inventario: list, limite: int = 5) -> list:
    """Retorna una lista de productos con stock menor al límite."""
    return [p for p in inventario if p['cantidad'] < limite]