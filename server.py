import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 12345

# Crear socket servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("🔵 Servidor iniciado... Esperando conexiones...")

clientes = []

def manejar_cliente(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if not mensaje:
                break
            print(f"📩 Mensaje recibido: {mensaje}")
            for c in clientes:
                c.send(mensaje.encode('utf-8'))
        except:
            break
    clientes.remove(cliente)
    cliente.close()

while True:
    cliente, direccion = server.accept()
    print(f"🟢 Nueva conexión desde {direccion}")
    clientes.append(cliente)
    hilo = threading.Thread(target=manejar_cliente, args=(cliente,))
    hilo.start()
