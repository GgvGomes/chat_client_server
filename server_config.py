import socket
import threading

HOST = 'localhost'
PORT = 12345

clients = []
running = True

def broadcast(message, sender_conn=None):
    for client in clients:
        conn, _ = client
        if conn != sender_conn:
            try:
                conn.sendall(message.encode())
            except:
                pass

def handle_client(conn, addr):
    print(f"[+] Conectado: {addr}")
    clients.append((conn, addr))
    try:
        while running:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            if msg.lower() == "sair":
                conn.sendall("Você foi desconectado pelo servidor.".encode())
                break
            print(f"[{addr}] {msg}")
            
            # Envia de volta ao cliente que enviou
            conn.sendall(f"Você disse: {msg}".encode())
            
            # Também pode enviar para outros (broadcast opcional)
            # broadcast(f"{addr}: {msg}", sender_conn=conn)
    except:
        pass
    finally:
        print(f"[-] Desconectado: {addr}")
        conn.close()
        clients.remove((conn, addr))

def listen_for_exit():
    global running
    while running:
        cmd = input()
        if cmd.strip().lower() == "sair":
            print("Encerrando servidor...")
            running = False
            for conn, _ in clients:
                try:
                    conn.sendall("Servidor encerrado.".encode())
                    conn.close()
                except:
                    pass
            break

def start_server():
    global running
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[Servidor iniciado em {HOST}:{PORT}]")
    
    # Thread para permitir desligamento do servidor via comando
    threading.Thread(target=listen_for_exit, daemon=True).start()

    try:
        while running:
            server.settimeout(1.0)
            try:
                conn, addr = server.accept()
                threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
            except socket.timeout:
                continue
    finally:
        server.close()
        print("Servidor finalizado.")
