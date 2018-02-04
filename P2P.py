import socket


class P2p_client:
    data_size = 1024
    sock = None
    host = None
    port = None

    connected = False

    def __init__(self, port, host=None, data_size=1024):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        if host is None:
            self.host = socket.gethostname()
        else:
            self.host = host
        self.connected = False
        self.data_size = data_size

    def connect_to(self, host):
        self.host = host
        if self.connected == True:
            self.close_socket()
        self.sock.connect((self.host, self.port))
        self.connected = True

    def send_msg(self, data, new_host=None):
        if new_host is not None:
            self.connect_to(new_host)
        self.sock.send(data.encode())
    
    def recv_msg(self, new_host=None):
        if new_host is not None:
            self.connect_to(new_host)
        data = self.sock.recv(self.data_size)
        return data

    def close_socket(self):
        self.sock.close()
        self.connected = False


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
        return data

    def close_socket(self):
        self.sock.close()


class P2p_entry:
    def __init__(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
