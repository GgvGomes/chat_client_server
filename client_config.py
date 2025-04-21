import socket
import threading

HOST = 'localhost'
PORT = 12345

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(f"\n{msg}")
        except:
            print("Erro ao receber mensagem ou conexão encerrada.")
            break

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Conectado ao servidor. Digite mensagens para enviar.")
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input()
        if msg.lower() == 'sair':
            client.close()
            break
        client.sendall(msg.encode())
