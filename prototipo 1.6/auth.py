import tkinter as tk
from tkinter import messagebox
from data import usuarios
from menu_cliente import abrir_menu_cliente
from menu_vendedor import abrir_menu_vendedor
from menu_admin import abrir_menu_admin

ventana_login = None
ventana_registro = None

def iniciar_sesion():
    global ventana_login
    if ventana_login is not None and ventana_login.winfo_exists():
        ventana_login.lift()
        return

    ventana_login = tk.Toplevel()
    ventana_login.title("Iniciar Sesión")
    ventana_login.geometry("300x200")

    tk.Label(ventana_login, text="Usuario").pack(pady=5)
    entry_usuario = tk.Entry(ventana_login)
    entry_usuario.pack(pady=5)

    tk.Label(ventana_login, text="Contraseña").pack(pady=5)
    entry_contraseña = tk.Entry(ventana_login, show="*")
    entry_contraseña.pack(pady=5)

    def validar():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()

        if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
            tipo = usuarios[usuario]["tipo"]
            ventana_login.destroy()

            if tipo == "cliente":
                abrir_menu_cliente(usuario)
            elif tipo == "vendedor":
                abrir_menu_vendedor(usuario)
            elif tipo == "admin":
                abrir_menu_admin(ventana_login)  # <-- Ya no pasamos ventana
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(ventana_login, text="Ingresar", command=validar).pack(pady=10)

def registrar():
    global ventana_registro
    if ventana_registro is not None and ventana_registro.winfo_exists():
        ventana_registro.lift()
        return

    ventana_registro = tk.Toplevel()
    ventana_registro.title("Crear Cuenta")
    ventana_registro.geometry("300x250")

    tk.Label(ventana_registro, text="Nuevo Usuario").pack(pady=5)
    entry_nuevo_usuario = tk.Entry(ventana_registro)
    entry_nuevo_usuario.pack(pady=5)

    tk.Label(ventana_registro, text="Contraseña").pack(pady=5)
    entry_nueva_contraseña = tk.Entry(ventana_registro, show="*")
    entry_nueva_contraseña.pack(pady=5)

    tk.Label(ventana_registro, text="Tipo de Usuario").pack(pady=5)
    tipo_var = tk.StringVar(value="cliente")
    opciones = ["cliente", "vendedor"]
    tk.OptionMenu(ventana_registro, tipo_var, *opciones).pack(pady=5)

    def crear():
        nuevo_usuario = entry_nuevo_usuario.get()
        nueva_contraseña = entry_nueva_contraseña.get()
        tipo = tipo_var.get()

        if nuevo_usuario in usuarios:
            messagebox.showerror("Error", "El usuario ya existe")
        elif not nuevo_usuario or not nueva_contraseña:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            usuarios[nuevo_usuario] = {"contraseña": nueva_contraseña, "tipo": tipo}
            messagebox.showinfo("Éxito", f"Usuario {nuevo_usuario} registrado como {tipo}")
            ventana_registro.destroy()

    tk.Button(ventana_registro, text="Registrar", command=crear).pack(pady=10)
