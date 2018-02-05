from . import P2p_client, P2p_server

class P2p_entry:
    entry_mode = -1

    client = None
    server = None

    def __init__(self, mode, server_port=None, data_size=1024):
        'Mode - 0 for client, 1 for server'
        if mode == 1 or mode == "server":
            self.mode = 1
            self.server = P2p_server.P2p_server(server_port, data_size=data_size)
        elif mode == 0 or mode == "client":
            self.mode = 0
            self.client = P2p_client.P2p_client(data_size=data_size)

    def start_client(self, host=None, port=None):
        if host is not None and port is not None:
            self.client.connect_to(host, port)

    def start_server(self):
        client_pair = self.server.accept_client()
        return client_pair

    def start(self, server_host=None, server_port=None):
        """
        For client, either connects to the server (if host and port are given), or does nothing is either is not given.
        For server, accepts client and returns client pair
        """
        if self.mode == 0:
            self.start_client(host=server_host, port=server_port)
            return None
        elif self.mode == 1:
            return self.start_server()

    def send_msg(self, data, client_pair=None, server_host=None, server_port=None):
        """
        Sends the msg depending on the mode.
        If the mode is 0 (client) the server host and server port is expected. If already connected from running 'start' server host and server port can be ignored to use previously used ones.
        If the mode is 1 (server) the client pair is expected. If not provided, server will wait to accept a client first
        """
        if self.mode == 0:
            self.send_msg_client(data, server_host, server_port)
        elif self.mode == 1:
            client_pair_accepted = self.send_msg_server(data, client_pair=client_pair)
            return client_pair_accepted

    def recv_msg(self, client_pair=None):
        """
        Receives a msg.
        If 0 (client), receives msg from the connected server. Needs to either be started with provided server host and port, or send msg to a given server. Return msg and None.
        If 1 (server), receives msg from given client pair. If no client pair given, accepts client. Returns msg and client pair from which it was received.
        """
        if self.mode == 0:
            data = self.recv_msg_client()
            return data, None
        elif self.mode == 1:
            data, client_pair = self.recv_msg_server(client_pair)
            return data, client_pair

    def close(self, client_pair=None):
        """
        Closes opened sockets.
        For the server, if client pair is given close the client's socket, instead of server's
        """
        if self.mode == 0:
            self.close_client()
        elif self.mode == 1:
            self.close_server(client_pair)

    def close_client(self):
        self.client.close_socket()

    def close_server(self, client_pair=None):
        if client_pair is None:
            self.server.close_socket()
        else:
            self.server.close_client(client_pair)

    def send_msg_client(self, data, host, port):
        self.client.send_msg(data, new_host=host, new_port=port)

    def recv_msg_client(self):
        received_data = self.client.recv_msg()
        return received_data

    def recv_msg_server(self, client_pair=None):
        if client_pair is None:
            client_pair = self.server.accept_client()
        received_data = self.server.recv_msg(client_pair)
        return received_data, client_pair

    def send_msg_server(self, data, client_pair=None):
        if client_pair is None:
            client_pair = self.server.accept_client()
        self.server.send_msg(data, client_pair)
        return client_pair
