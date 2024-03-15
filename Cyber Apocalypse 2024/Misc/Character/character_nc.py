import socket

def interact_with_netcat_server(server_host, server_port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the Netcat server
        client_socket.connect((server_host, server_port))
        
        print("Connected to the server. You can start sending data. Press Ctrl+C to exit.")
        
        got_flag = False
        # Continuously interact with the server
        while True:
            f = open('nc_output', 'a')
            # Send data to the server
            for i in range(1, 104):
                if i == 103:
                    got_flag = True
                message = str(i) + '\n'
                client_socket.sendall(message.encode())
            
            # Receive data from the server
            received_data = client_socket.recv(1024).decode()
            f.writelines(received_data)
            if got_flag:
                break
        print("Flag acquired.")
        f.close()

    except KeyboardInterrupt:
        print("stop")
    finally:
        # Close the connection
        client_socket.close()

# Define the host and port of the Netcat server
server_host = '94.237.53.58'  # Change this to your server's IP address
server_port = 46859         # Change this to your server's port

# Call the function to interact with the Netcat server
interact_with_netcat_server(server_host, server_port)

f = open('nc_output', 'r')

x = ''
for line in f:
    x += line[-2]

print(x)