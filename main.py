import sys

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["client", "server"]:
        print("Uso: python main.py [client|servidor]")
        return

    if sys.argv[1] == "server":
        import server_setup
        server_setup.run_server()
    else:
        import client_config
        client_config.run_client()

if __name__ == "__main__":
    main()
