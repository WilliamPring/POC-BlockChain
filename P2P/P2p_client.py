import socket


class P2p_client:
    data_size = 1024
    sock = None
    host = None
    port = None

    connected = False
    socket_open = False

    def __init__(self, data_size=1024):
        self.do_socket_creation()
        
        self.connected = False
        self.data_size = data_size

    def do_socket_creation(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_open = True

    def connect_to(self, host, port):
        self.host = host
        self.port = port
        if self.connected == True:
            self.close_socket()
        if self.socket_open == False:
            self.do_socket_creation()
        self.sock.connect((self.host, self.port))
        self.connected = True

    def send_msg(self, data, new_host=None, new_port=None):
        if new_host is not None or new_port is not None:
            if new_host != self.host or new_port != self.port:
                host = new_host if new_host is not None else self.host
                port = new_port if new_port is not None else self.port
                self.connect_to(host, port)
        self.sock.send(data.encode())
    
    def recv_msg(self):
        data = self.sock.recv(self.data_size)
        return data.decode('utf-8')

    def close_socket(self):
        self.sock.close()
        self.connected = False
        self.socket_open = False
        self.host = None
        self.port = None
