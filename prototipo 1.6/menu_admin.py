import tkinter as tk
from tkinter import messagebox
import csv
import os
import main
from data import usuarios  

USUARIOS_FILE = "usuarios.csv"
PRODUCTOS_FILE = "productos.csv"

def abrir_menu_admin(ventana_actual):
    ventana_actual.destroy()
    ventana = tk.Tk()
    ventana.title("Menú Admin")

    tk.Label(ventana, text="Menú Administrador", font=("Arial", 16)).pack(pady=10)

    tk.Button(ventana, text="Ver usuarios registrados", width=30, command=ver_usuarios).pack(pady=5)
    tk.Button(ventana, text="Eliminar usuario", width=30, command=eliminar_usuario).pack(pady=5)
    tk.Button(ventana, text="Cerrar sesión", width=30, command=lambda: cerrar_sesion(ventana)).pack(pady=20)

def ver_usuarios():
    ventana = tk.Toplevel()
    ventana.title("Usuarios Registrados")

    usuarios_registrados = [f"{nombre} ({info['tipo']})" for nombre, info in usuarios.items() if nombre != "admin"]

    if usuarios_registrados:
        for usuario in usuarios_registrados:
            tk.Label(ventana, text=usuario).pack(anchor="w", padx=10)
    else:
        tk.Label(ventana, text="No hay usuarios registrados.").pack()

def eliminar_usuario():
    ventana = tk.Toplevel()
    ventana.title("Eliminar Usuario")

    tk.Label(ventana, text="Nombre de usuario a eliminar:").pack()
    entry = tk.Entry(ventana)
    entry.pack()

    def eliminar():
        usuario_eliminar = entry.get()
        if usuario_eliminar == "admin":
            messagebox.showerror("Error", "No se puede eliminar al administrador.")
            return

        eliminado = False

        # Eliminar del archivo usuarios
        with open(USUARIOS_FILE, newline='', encoding='utf-8') as f:
            usuarios = list(csv.DictReader(f))

        with open(USUARIOS_FILE, "w", newline='', encoding='utf-8') as f:
            fieldnames = ["Usuario", "Contraseña", "Rol"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in usuarios:
                if row["Usuario"] != usuario_eliminar:
                    writer.writerow(row)
                else:
                    eliminado = True

        # También eliminar productos de ese usuario si es vendedor
        if eliminado and os.path.exists(PRODUCTOS_FILE):
            with open(PRODUCTOS_FILE, newline='', encoding='utf-8') as f:
                productos = list(csv.DictReader(f))

            with open(PRODUCTOS_FILE, "w", newline='', encoding='utf-8') as f:
                fieldnames = ["ID", "Nombre", "Consola", "Precio", "Ubicación", "Vendedor"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for p in productos:
                    if p["Vendedor"] != usuario_eliminar:
                        writer.writerow(p)

        if eliminado:
            messagebox.showinfo("Éxito", f"Usuario '{usuario_eliminar}' eliminado.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")

    tk.Button(ventana, text="Eliminar", command=eliminar).pack(pady=10)

def cerrar_sesion(ventana):
    ventana.destroy()
    main.main()
