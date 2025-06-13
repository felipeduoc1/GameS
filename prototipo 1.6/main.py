import tkinter as tk
import auth

def main():
    root = tk.Tk()
    root.title("Sistema de Venta de Videojuegos")
    root.geometry("400x300")

    tk.Label(root, text="🎮 Bienvenido", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Iniciar Sesión", width=25, command=auth.iniciar_sesion).pack(pady=10)
    tk.Button(root, text="Crear Cuenta", width=25, command=auth.registrar).pack(pady=10)
    tk.Button(root, text="Salir", width=25, command=root.quit).pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    main()
