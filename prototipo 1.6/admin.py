from tkinter import simpledialog, messagebox
from data import usuarios

def ver_usuarios():
    if not usuarios:
        messagebox.showinfo("Usuarios", "No hay usuarios registrados.")
        return
    texto = ""
    for nombre, info in usuarios.items():
        texto += f"{nombre} - {info['tipo'].capitalize()}\n"
    messagebox.showinfo("Usuarios Registrados", texto)

def eliminar_usuario():
    nombre = simpledialog.askstring("Eliminar Usuario", "Ingrese el nombre del usuario a eliminar:")
    if nombre:
        if nombre in usuarios and usuarios[nombre]["tipo"] != "admin":
            del usuarios[nombre]
            messagebox.showinfo("Éxito", f"Usuario '{nombre}' eliminado.")
        elif nombre in usuarios and usuarios[nombre]["tipo"] == "admin":
            messagebox.showwarning("Denegado", "No se puede eliminar al administrador.")
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")
