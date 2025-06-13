import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

RUTA_PRODUCTOS = "productos.csv"
RUTA_HISTORIAL = "historial.csv"

# Función 1: Buscar productos con filtros opcionales
def buscar_productos():
    def aplicar_filtros():
        nombre = entry_nombre.get().strip().lower()
        consola = entry_consola.get().strip().lower()
        ubicacion = entry_ubicacion.get().strip().lower()
        genero = entry_genero.get().strip().lower()
        anio = entry_anio.get().strip()

        resultados.delete(*resultados.get_children())
        with open(RUTA_PRODUCTOS, newline="", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                if (
                    (not nombre or nombre in fila["nombre"].lower())
                    and (not consola or consola in fila["consola"].lower())
                    and (not ubicacion or ubicacion in fila["ubicacion"].lower())
                    and (not genero or genero in fila["genero"].lower())
                    and (not anio or anio == fila["anio"])
                ):
                    resultados.insert("", "end", values=list(fila.values()))

    def comprar_producto():
        selected_item = resultados.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un producto para comprar.")
            return

        producto = resultados.item(selected_item, "values")
        nombre, consola, precio, ubicacion, genero, anio, stock, vendedor = producto

        if int(stock) <= 0:
            messagebox.showerror("Error", "El producto seleccionado no tiene stock disponible.")
            return

        # Registrar la compra en el historial
        with open(RUTA_HISTORIAL, "a", newline="", encoding="utf-8") as archivo_historial:
            writer = csv.writer(archivo_historial)
            writer.writerow([nombre, consola, precio, ubicacion, genero, anio, vendedor])

        # Actualizar el stock en productos.csv
        productos_actualizados = []
        with open(RUTA_PRODUCTOS, newline="", encoding="utf-8") as archivo_productos:
            reader = csv.DictReader(archivo_productos)
            for fila in reader:
                if fila["nombre"] == nombre and fila["consola"] == consola:
                    fila["stock"] = str(int(fila["stock"]) - 1)
                productos_actualizados.append(fila)

        with open(RUTA_PRODUCTOS, "w", newline="", encoding="utf-8") as archivo_productos:
            writer = csv.DictWriter(archivo_productos, fieldnames=productos_actualizados[0].keys())
            writer.writeheader()
            writer.writerows(productos_actualizados)

        messagebox.showinfo("Éxito", "Compra realizada con éxito.")
        aplicar_filtros()  # Actualizar la lista de resultados

    ventana = tk.Toplevel()
    ventana.title("Buscar Juegos")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana, text="Consola:").grid(row=1, column=0)
    entry_consola = tk.Entry(ventana)
    entry_consola.grid(row=1, column=1)

    tk.Label(ventana, text="Ubicación:").grid(row=2, column=0)
    entry_ubicacion = tk.Entry(ventana)
    entry_ubicacion.grid(row=2, column=1)

    tk.Label(ventana, text="Género:").grid(row=3, column=0)
    entry_genero = tk.Entry(ventana)
    entry_genero.grid(row=3, column=1)

    tk.Label(ventana, text="Año:").grid(row=4, column=0)
    entry_anio = tk.Entry(ventana)
    entry_anio.grid(row=4, column=1)

    tk.Button(ventana, text="Buscar", command=aplicar_filtros).grid(row=5, column=0, columnspan=2, pady=10)

    columnas = ["nombre", "consola", "precio", "ubicacion", "genero", "anio", "stock", "vendedor"]
    resultados = ttk.Treeview(ventana, columns=columnas, show="headings")
    for col in columnas:
        resultados.heading(col, text=col.capitalize())
        resultados.column(col, width=100)
    resultados.grid(row=6, column=0, columnspan=2)

    tk.Button(ventana, text="Comprar", command=comprar_producto).grid(row=7, column=0, columnspan=2, pady=10)

# Función 2: Ver historial de compras (simulación)
def ver_historial_compras(usuario):
    ventana = tk.Toplevel()
    ventana.title("Historial de Compras")

    if not os.path.exists(RUTA_HISTORIAL):
        tk.Label(ventana, text="No hay historial de compras.").pack()
        return

    with open(RUTA_HISTORIAL, newline="", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            tk.Label(ventana, text=", ".join(fila)).pack()

# Función 3: Simulación básica de chat
def abrir_chat_vendedor():
    ventana = tk.Toplevel()
    ventana.title("Chat con Vendedor")
    tk.Label(ventana, text="Chat de prueba. No funcional.").pack(pady=10)
    tk.Entry(ventana).pack()
    tk.Button(ventana, text="Enviar", command=lambda: messagebox.showinfo("Mensaje", "Mensaje enviado.")).pack(pady=5)

# Función 4: Dashboard para cliente
def generar_dashboard_cliente():
    ventana = tk.Toplevel()
    ventana.title("Dashboard Cliente")

    conteo_consolas = {}
    if not os.path.exists(RUTA_PRODUCTOS):
        tk.Label(ventana, text="No hay productos.").pack()
        return

    with open(RUTA_PRODUCTOS, newline="", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            consola = fila["consola"]
            conteo_consolas[consola] = conteo_consolas.get(consola, 0) + 1

    for consola, cantidad in conteo_consolas.items():
        tk.Label(ventana, text=f"{consola}: {cantidad} juegos").pack()

