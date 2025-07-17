import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 12345

# Crear socket cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Función para recibir mensajes
def recibir_mensajes():
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            chat.config(state='normal')
            chat.insert(tk.END, mensaje + "\n")
            chat.config(state='disabled')
            chat.yview(tk.END)
        except:
            break

# Función para enviar mensajes
def enviar_mensaje():
    mensaje = entrada.get()
    if mensaje:
        mensaje_completo = f"{nombre_usuario}: {mensaje}"
        cliente.send(mensaje_completo.encode('utf-8'))
        entrada.delete(0, tk.END)

# Crear interfaz con Tkinter
ventana = tk.Tk()
ventana.title("Chat Cliente - Maria")

# Pedir nombre al usuario
nombre_usuario = simpledialog.askstring("Nombre", "Maria:", parent=ventana)
if not nombre_usuario:
    messagebox.showinfo("Info", "Se debe ingresar un nombre.")
    ventana.destroy()
    exit()

# Cuadro de chat
chat = tk.Text(ventana, height=15, width=50, state='disabled')
chat.pack(padx=10, pady=10)

# Entrada de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(padx=10, pady=5)

# Botón enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=(0, 10))

# Cierre correcto
def cerrar_ventana():
    cliente.close()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Hilo para recibir mensajes
hilo = threading.Thread(target=recibir_mensajes)
hilo.daemon = True
hilo.start()

ventana.mainloop()
