import tkinter as tk
from cliente import buscar_productos as buscar_juegos_filtro, ver_historial_compras, abrir_chat_vendedor, generar_dashboard_cliente

ventana_cliente = None

def abrir_menu_cliente(usuario):
    global ventana_cliente
    if ventana_cliente is not None and ventana_cliente.winfo_exists():
        ventana_cliente.lift()
        return

    ventana_cliente = tk.Toplevel()
    ventana_cliente.title("Menú Cliente")
    ventana_cliente.geometry("400x400")

    tk.Label(ventana_cliente, text=f"Bienvenido, {usuario}", font=("Arial", 14)).pack(pady=10)

    # Se eliminó el argumento 'usuario' para evitar el TypeError
    tk.Button(ventana_cliente, text="🔍 Buscar juegos", width=30,
              command=buscar_juegos_filtro).pack(pady=5)

    tk.Button(ventana_cliente, text="📜 Historial de compras", width=30,
              command=lambda: ver_historial_compras(usuario)).pack(pady=5)

    tk.Button(ventana_cliente, text="💬 Chat con vendedor", width=30,
              command=lambda: abrir_chat_vendedor(usuario)).pack(pady=5)

    tk.Button(ventana_cliente, text="📊 Dashboard", width=30,
              command=lambda: generar_dashboard_cliente(usuario)).pack(pady=5)

    def cerrar_sesion():
        ventana_cliente.destroy()

    tk.Button(ventana_cliente, text="🔙 Cerrar sesión", width=30, command=cerrar_sesion).pack(pady=20)
