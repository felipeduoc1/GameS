import tkinter as tk
from tkinter import messagebox
import csv
import os

PRODUCTOS_FILE = "productos.csv"

# Encabezados reales del CSV
ENCABEZADOS = ["nombre", "consola", "precio", "ubicacion", "genero", "anio", "stock", "vendedor"]

# Asegura que el archivo tenga encabezado correcto
def inicializar_productos():
    if not os.path.exists(PRODUCTOS_FILE):
        with open(PRODUCTOS_FILE, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=ENCABEZADOS)
            writer.writeheader()

inicializar_productos()

def agregar_producto(vendedor):
    ventana = tk.Toplevel()
    ventana.title("Agregar Producto")

    campos = ["nombre", "consola", "precio", "ubicacion", "genero", "anio", "stock"]
    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(ventana, text=campo.capitalize() + ":").grid(row=i, column=0)
        entrada = tk.Entry(ventana)
        entrada.grid(row=i, column=1)
        entradas[campo] = entrada

    def guardar():
        for campo in campos:
            if not entradas[campo].get():
                messagebox.showerror("Error", f"El campo {campo} es obligatorio.")
                return

        try:
            float(entradas["precio"].get())
            int(entradas["anio"].get())
            int(entradas["stock"].get())
        except ValueError:
            messagebox.showerror("Error", "Precio, año y stock deben ser numéricos.")
            return

        with open(PRODUCTOS_FILE, "a", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=ENCABEZADOS)
            fila = {campo: entradas[campo].get() for campo in campos}
            fila["vendedor"] = vendedor
            writer.writerow(fila)

        messagebox.showinfo("Éxito", "Producto guardado con éxito")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=len(campos), column=0, columnspan=2, pady=10)

def ver_productos_del_vendedor(vendedor):
    productos = []
    with open(PRODUCTOS_FILE, "r", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for p in reader:
            if p.get("vendedor") == vendedor:
                productos.append(p)
    return productos

def editar_producto(vendedor):
    productos = ver_productos_del_vendedor(vendedor)
    if not productos:
        messagebox.showinfo("Editar", "No tienes productos para editar.")
        return

    ventana = tk.Toplevel()
    ventana.title("Editar Producto")

    tk.Label(ventana, text="Nombre exacto del producto:").grid(row=0, column=0)
    nombre_entry = tk.Entry(ventana)
    nombre_entry.grid(row=0, column=1)

    tk.Label(ventana, text="Nuevo Precio:").grid(row=1, column=0)
    nuevo_precio = tk.Entry(ventana)
    nuevo_precio.grid(row=1, column=1)

    def editar():
        editado = False
        nombre_target = nombre_entry.get()
        with open(PRODUCTOS_FILE, "r", newline='', encoding='utf-8') as f:
            reader = list(csv.DictReader(f))

        with open(PRODUCTOS_FILE, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=ENCABEZADOS)
            writer.writeheader()
            for row in reader:
                if row["nombre"] == nombre_target and row["vendedor"] == vendedor:
                    row["precio"] = nuevo_precio.get()
                    editado = True
                writer.writerow(row)

        if editado:
            messagebox.showinfo("Éxito", "Producto editado con éxito")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "No se encontró el producto con ese nombre o no te pertenece")

    tk.Button(ventana, text="Editar", command=editar).grid(row=2, column=0, columnspan=2)

def eliminar_producto(vendedor):
    productos = ver_productos_del_vendedor(vendedor)
    if not productos:
        messagebox.showinfo("Eliminar", "No tienes productos para eliminar.")
        return

    ventana = tk.Toplevel()
    ventana.title("Eliminar Producto")

    tk.Label(ventana, text="Nombre exacto del producto a eliminar:").grid(row=0, column=0)
    nombre_entry = tk.Entry(ventana)
    nombre_entry.grid(row=0, column=1)

    def eliminar():
        eliminado = False
        nombre_target = nombre_entry.get()
        with open(PRODUCTOS_FILE, "r", newline='', encoding='utf-8') as f:
            reader = list(csv.DictReader(f))

        with open(PRODUCTOS_FILE, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=ENCABEZADOS)
            writer.writeheader()
            for row in reader:
                if row["nombre"] == nombre_target and row["vendedor"] == vendedor:
                    eliminado = True
                    continue
                writer.writerow(row)

        if eliminado:
            messagebox.showinfo("Éxito", "Producto eliminado con éxito")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "No se encontró el producto con ese nombre o no te pertenece")

    tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=1, column=0, columnspan=2)

def generar_dashboard_vendedor(vendedor):
    productos = ver_productos_del_vendedor(vendedor)
    return len(productos)
