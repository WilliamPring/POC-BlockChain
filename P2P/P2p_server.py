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

    socket_open = False

    def __init__(self, port, data_size=1024):
        self.do_socket_creation()

        self.data_size = data_size
        self.host = socket.gethostname()
        self.port = port

        self.do_binding()

    def do_socket_creation(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def do_binding(self):
        self.sock.bind((self.host, self.port))
        self.socket_open = True
        self.sock.listen(5)

    def accept_client(self):
        if self.socket_open == False:
            self.do_socket_creation()
            self.do_binding()
        client_sock, client_addr = self.sock.accept()
        client_pair = P2p_client_pair(client_sock, client_addr)
        return client_pair

    def send_msg(self, data, client_pair):
        client_pair.socket.send(data.encode())

    def recv_msg(self, client_pair):
        data = client_pair.socket.recv(self.data_size)
        return data.decode('utf-8')

    def close_client(self, client_pair):
        client_pair.socket.close()

    def close_socket(self):
        self.sock.close()
        self.socket_open = False

