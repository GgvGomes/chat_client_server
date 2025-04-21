import socket
import threading

HOST = 'localhost'
PORT = 12345

def handle_client(conn, addr):
    print(f"[+] Nova conexão de {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"{addr}: {msg}")
            conn.sendall(f"Servidor recebeu: {msg}".encode())
        except ConnectionResetError:
            break
    conn.close()
    print(f"[-] Conexão encerrada: {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor escutando em {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
