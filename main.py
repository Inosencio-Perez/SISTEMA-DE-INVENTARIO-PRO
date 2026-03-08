"""
Punto de entrada principal del Sistema de Inventario Pro.
Gestiona el menú y la interacción con el usuario.
"""
import funciones
import datos
import os

def limpiar_pantalla():
    #Limpia la terminal según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    # 1. Cargamos los datos al iniciar
    inventario = datos.cargar_datos()
    
    while True:
        limpiar_pantalla()
        print("=== 📦 SISTEMA DE INVENTARIO PRO ===")
        print("1. Ver Inventario")
        print("2. Agregar Producto")
        print("3. Buscar Bajo Stock")
        print("4. Guardar y Salir")
        print("====================================")
        
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            print("\n--- Listado de Productos ---")
            if not inventario:
                print("El inventario está vacío.")
            for p in inventario:
                print(f"ID: {inventario.index(p)} | {p['nombre']} | Stock: {p['cantidad']} | Precio: ${p['precio']:.2f}")
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            try:
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad inicial: "))
                precio = float(input("Precio unitario: "))
                
                # Usamos la función del módulo funciones.py
                inventario = funciones.agregar_producto(inventario, nombre, cantidad, precio)
                print("✅ Producto añadido temporalmente.")
            except ValueError:
                print("❌ Error: Cantidad y Precio deben ser números.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            # Demostramos el uso de argumentos por defecto
            bajo_stock = funciones.buscar_bajo_stock(inventario)
            print("\n--- ⚠️ Productos con bajo stock (< 5) ---")
            for p in bajo_stock:
                print(f"{p['nombre']} (Solo quedan {p['cantidad']})")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            # Guardamos físicamente antes de cerrar
            datos.guardar_datos(inventario)
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()

# Fin del programa