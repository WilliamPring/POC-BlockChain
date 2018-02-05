from P2P import P2p_entry

if __name__ == '__main__':
    entry = P2p_entry.P2p_entry('client')

    entry.start(server_host='arch-pc', server_port=25255)
    entry.send_msg("hello from client part")
    data, temp = entry.recv_msg()
    print(data)
    entry.close()

    entry.start(server_host='arch-pc', server_port=25255)
    entry.send_msg("hello from client part 2")
    data, temp = entry.recv_msg()
    print(data)
    entry.close()
