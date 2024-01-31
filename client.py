import socket

def start_client():
    server_address = ('localhost', 8000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    while True:
        req = input("Введите название хоста (или 'close' для выхода): ")
        if req == 'close':
            break

        try:
            client_socket.send(req.encode())

            try:
                res = client_socket.recv(1024).decode()
                print(res)
            except Exception as e:
                print("Произошла ошибка при получении ответа:", str(e))
                continue

        except socket.error as e:
            print("Произошла ошибка при подключении к серверу:", str(e))
            continue

        except Exception as e:
            print("Произошла ошибка:", str(e))
            continue

    client_socket.close()

start_client()

