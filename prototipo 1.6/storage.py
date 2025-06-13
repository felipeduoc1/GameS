import csv

# Diccionario de usuarios registrados
# Ejemplo: {"cliente01": {"clave": "1234", "tipo": "cliente"}}
usuarios = {}

# Lista de productos cargados desde el archivo CSV
productos = []

# Cargar productos desde productos.csv al iniciar
def cargar_productos():
    global productos
    try:
        with open("productos.csv", newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            productos = [dict(fila) for fila in lector]

            # Convertimos tipos (precio, anio, stock)
            for prod in productos:
                prod["precio"] = float(prod["precio"])
                prod["anio"] = int(prod["anio"])
                prod["stock"] = int(prod["stock"])
    except FileNotFoundError:
        print("⚠️ Archivo productos.csv no encontrado.")
    except Exception as e:
        print(f"⚠️ Error al cargar productos: {e}")

# Historial de compras: {"cliente01": [{"nombre": ..., "precio": ...}, ...]}
historial_compras = {}

# Carritos de clientes: {"cliente01": [{"nombre": ..., "precio": ..., "stock": ...}, ...]}
carritos = {}

# Mensajes: {"cliente01": [{"de": "cliente01", "para": "vendedor01", "mensaje": "..."}, ...]}
mensajes = {}

# Ejecutamos la carga de productos al importar el módulo
cargar_productos()
