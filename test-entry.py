from P2P import P2p_entry

if __name__ == '__main__':
    entry = P2p_entry.P2p_entry("server", server_port=25255)

    pair = entry.start()
    data, temp = entry.recv_msg(client_pair=pair)
    print(data)
    entry.send_msg("hello from the server part", client_pair=pair)
    entry.close(client_pair=pair)
    entry.close()

    pair = entry.start()
    data, temp = entry.recv_msg(client_pair=pair)
    print(data)
    entry.send_msg("hello from the server part 2", client_pair=pair)
    entry.close(client_pair=pair)
    entry.close()
