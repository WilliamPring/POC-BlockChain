from P2P import P2p_client 


if __name__ == '__main__':
    client = P2p_client.P2p_client(25255)
    client.connect_to("arch-pc")
    client.send_msg("hello from client")
    print(client.recv_msg())
    client.close_socket()
