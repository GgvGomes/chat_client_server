# Chat Simples em Python (Cliente e Servidor via Linha de Comando)

Este é um chat básico feito em Python usando `sockets`, com comunicação entre cliente e servidor via linha de comando.

## 📦 Requisitos

- Python 3.6+
- Nenhuma biblioteca externa (usa apenas bibliotecas padrão)

## 🛠️ Estrutura

- `main.py`: ponto de entrada para o projeto (escolhe entre cliente ou servidor)
- `server_setup.py`: inicializa o servidor
- `server_config.py`: lida com múltiplas conexões e gerenciamento de mensagens no servidor
- `client_config.py`: conecta ao servidor e envia/recebe mensagens

## 🚀 Como Usar

### 1. Rodar o servidor

```bash
python main.py server
```

### 2. Criar clientes

```bash
python main.py client
```

### 3. Enviar e exibir mensagens

Quando o cliente enviar uma mensagem, ele verá na linha de comando dele que a mensagem foi enviada.
O servidor receberá a mensagem e exibirá a mensagem contendo quem a enviou (IP e Porta).
Podem ser criados vários clientes, atualmente os clientes não conseguem se comunicar entre si.
