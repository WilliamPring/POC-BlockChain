import socket


class P2p_client_pair:
    socket = None
    address = None

    def __init__(self, sock, addr):
        self.socket = sock
        self.address = addr


class P2p_server:
    data_size = 1024
    sock = None
    host = None
    port = None

    def __init__(self, port, data_size=1024):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data_size = data_size
        self.host = socket.gethostname()
        self.port = port

        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

    def accept_client(self):
        client_sock, client_addr = self.sock.accept()
        client_pair = P2p_client_pair(client_sock, client_addr)
        return client_pair

    def send_msg(self, data, client_pair):
        client_pair.socket.send(data.encode())

    def recv_msg(self, client_pair):
        data = client_pair.socket.recv(self.data_size)
        return data.decode('utf-8')

    def close_socket(self):
        self.sock.close()

