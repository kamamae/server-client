import socket
import threading

def handle_client(client_socket, addr):
    print("Подключился клиент:", addr)

    try:
        while True:
            req = client_socket.recv(1024).decode()
            if not req or req == 'close':
                break

            try:
                res = socket.gethostbyname(req)
                client_socket.send(res.encode())
            except socket.gaierror as e:
                print("Ошибка разрешения имени хоста:", str(e))
                client_socket.send("Ошибка разрешения имени хоста".encode())

    except Exception as e:
        print("Произошла ошибка при обработке запроса:", str(e))
        client_socket.send("Ошибка при обработке запроса".encode())

    finally:
        client_socket.close()
        print("Соединение с клиентом закрыто:", addr)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(5)

    print("Сервер запущен")

    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

start_server()

