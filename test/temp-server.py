from P2P import P2p_server

if __name__ == '__main__':
    server = P2p_server.P2p_server(25255)
    client_pair = server.accept_client()
    print(server.recv_msg(client_pair))
    server.send_msg("hello from server", client_pair)
    server.close_socket()
