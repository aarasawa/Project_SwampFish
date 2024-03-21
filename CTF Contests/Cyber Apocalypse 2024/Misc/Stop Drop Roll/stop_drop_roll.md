# Stop Drop and Roll 

#### Difficulty: <code>Very Easy</code>

#### Description
> The Fray: The Video Game is one of the greatest hits of the last... well, we don't remember quite how long. Our "computers" these days can't run much more than that, and it has a tendency to get repetitive...

#### 1.
> I started with with using the socket library to communicate with the netcat server, parse output received from our responses, and reply. However, ran into a buffer blocking issue that turned into either a failed question or the connection being blocked. So I had to space replies using a timer. This worked but at a really slow pace.

``` python
import socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_host, server_port))
        print("Connected to server. You can start sending data. Press Ctrl + C to exit.")

        ...

        while True:
            recv_data = client_socket.recv(1024).decode()
            f.writelines(recv_data)
            if recv_data[0:4]  == "====":
                message = "y\n"
                client_socket.sendall(message.encode())
            ...
```

#### 2. 
> The official writeup imported <code>pwn</code> instead of <code>socket</code>. Pwntools also has built-in remoting tools for connecting to sockets. Comparing the two snippets above and below, its much more readable and user friendly.

``` python
from pwn import *
    p = remote('83.136.252.32', 46312)

    p.sendlineafter(b'(y/n) ', b'y')
    p.recvline()
```