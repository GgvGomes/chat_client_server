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
python main.py servidor
```
