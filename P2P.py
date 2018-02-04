import socket


class P2p_base:
    data_size = 1024
    sock = None
    host = None
    port = None

    def __init__(self, port, host=None, data_size=1024):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        if host is None:
            self.host = socket.gethostname()
        else:
            self.host = host
        self.data_size = data_size


class P2p_client(P2p_base):
    connected = False

    def __init__(self, port):
        super().__init__(port)

    def connect_to(self, host):
        super().host = host
        if self.connected == True:
            self.close_socket()
        super().sock.connect((super().host, super().port))
        self.connected = True

    def send_msg(self, data, new_host=None):
        if new_host is not None:
            self.connect_to(new_host)
        super().sock.send(data)
    
    def recv_msg(self, new_host=None):
        if new_host is not None:
            self.connect_to(new_host)
        data = super().sock.recv(super().data_size)
        return data

    def close_socket(self):
        super().sock.close()
        self.connected = False


class P2p_client_pair:
    socket = None
    address = None

    def __init__(self, sock, addr):
        self.socket = sock
        self.address = addr


class P2p_server(P2p_base):
    def __init__(self, port):
        super().__init__(port)
        super().sock.bind((super().host, super().port))
        super().sock.listen(5)

    def accept_client(self):
        client_sock, client_addr = super().sock.accept()
        client_pair = P2p_client_pair(client_sock, client_addr)

    def send_msg(self, data, client_pair):
        pass

    def close_socket(self):
        super().sock.close()

class P2p_entry:
    def __init__(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
