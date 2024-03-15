import socket
import re
import time

commands = {
    'GORGE' : 'STOP',
    'PHREAK' : 'DROP',
    'FIRE' : 'ROLL'
}

server_host = '94.237.63.128'
server_port = 48219

def parse_SDR(msg):
    p = re.split('[ \n,]+', msg)
    p = [x for x in p if x in ["GORGE", "PHREAK", "FIRE"]]
    if len(p) > 0 and len(p) < 2:
        return commands[p[0]] + '\n'
    else:
        q = [commands[x] for x in p]
        return "-".join(q) + '\n'
    

def stop_drop_roll_server(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_host, server_port))
        print("Connected to server. You can start sending data. Press Ctrl + C to exit.")

        f = open('sdr_nc_out', 'w')

        while True:
            recv_data = client_socket.recv(1024).decode()
            f.writelines(recv_data)
            if recv_data[0:4]  == "====":
                message = "y\n"
                client_socket.sendall(message.encode())
            else:
                message = parse_SDR(recv_data)
                f.writelines(message)
                client_socket.sendall(message.encode())
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nInterrupted . . .")
    finally:
        client_socket.close()

stop_drop_roll_server(server_host, server_port)