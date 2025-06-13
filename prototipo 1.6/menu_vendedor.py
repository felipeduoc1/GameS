import tkinter as tk
from tkinter import messagebox
from vendedor import (
    agregar_producto,
    ver_productos_del_vendedor,
    editar_producto,
    eliminar_producto,
    generar_dashboard_vendedor
)

def abrir_menu_vendedor(usuario):
    ventana = tk.Toplevel()
    ventana.title("Menú Vendedor")

    tk.Label(ventana, text=f"Bienvenido vendedor: {usuario}", font=("Arial", 14)).pack(pady=10)

    tk.Button(ventana, text="Agregar Producto", width=30, command=lambda: agregar_producto(usuario)).pack(pady=5)
    tk.Button(ventana, text="Ver Mis Productos", width=30, command=lambda: mostrar_productos(usuario)).pack(pady=5)
    tk.Button(ventana, text="Editar Producto", width=30, command=lambda: editar_producto(usuario)).pack(pady=5)
    tk.Button(ventana, text="Eliminar Producto", width=30, command=lambda: eliminar_producto(usuario)).pack(pady=5)
    tk.Button(ventana, text="Dashboard", width=30, command=lambda: mostrar_dashboard(usuario)).pack(pady=5)
    tk.Button(ventana, text="Cerrar sesión", width=30, command=ventana.destroy).pack(pady=20)

def mostrar_productos(vendedor):
    productos = ver_productos_del_vendedor(vendedor)
    if not productos:
        messagebox.showinfo("Mis productos", "No tienes productos registrados.")
        return

    ventana = tk.Toplevel()
    ventana.title("Mis Productos")

    for p in productos:
        texto = (
            f"{p['nombre']} ({p['consola']}) - ${p['precio']} - "
            f"{p['ubicacion']} - {p['genero']} - Año: {p['anio']} - Stock: {p['stock']}"
        )
        tk.Label(ventana, text=texto).pack()

def mostrar_dashboard(vendedor):
    total = generar_dashboard_vendedor(vendedor)
    messagebox.showinfo("Dashboard", f"Tienes {total} productos publicados.")
