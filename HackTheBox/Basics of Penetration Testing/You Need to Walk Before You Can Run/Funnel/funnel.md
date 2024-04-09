# Funnel

#### Difficulty:<code>Very Easy</code>

#### Machine Tags:
  FTP  
  PostgreSQL  
  Reconnaissance  
  Tunneling  
  Password Spraying  
  Port Forwarding  
  Anon/Guest Access  
  Clear Text Credentials  

#### Description
  Access PostgreSQL database and use tunneling to access internal services on the network itself. 

#### **Tunneling**
  *Tunneling* protocol is a communication protocol for data to move from one network to another by exploiting encapsulation. Tunneling can be used to access resources available only to internal networks. SSH or *Secure Shell Protocol* is used for accessing remote systems in secure ways. The *client* is the machine that initiates the connection, and the *server* is the machine that receives the connection. 

  *Local Port Forwarding* is type of tunneling where a separate tunnel is created inside the existing SSH session to forward network traffic from a local port on the client's machine over to the remote server's port. 

  *Remote Port Forwarding* is a type of tunneling a.k.a *Reverse Tunneling* creates a separate tunnel from which SSH redirects incoming traffic to the server's port back to the client.

  *Dynamic Port Forwarding* uses *dynamic tunneling* for users to specify one port to forward incoming traffic from the client to the server dynamically. Dynamic tunneling relies on <code>SOCKS5</code>. 

#### **SOCKS**
  *SOCKS* is an internet protocol to exchange network packets between a client and server through a proxy server. Authentication is optional.

#### **Enumeration**
  Open ports are: 21/tcp : vsftpd 3.0.3, 22/tcp OpenSSH 8.2p1 Ubuntu. One of the scripts we used shows that anon FTP login are allowed.

#### **FTP Access**
  We can use anonymous credentials to login to the FTP server on the target machine. There are a couple files availabe on the directory we find through FTP. A few things we see, are a couple internal IDs plus the organization domain. Some usernames are: root, optimus, albert, andreas, christine, and maria. The other doc is about password creation guidelines: password must be unique, complex. Default password: funnel123#!# must be changed immediately. 

#### **Password Spraying**
  We have a handful of usernames and a default password. *Password spraying* is a brute-force attack with username-password combinations. <code>Hydra</code> is a tool we can use for password spraying. Typical countermeasures are to lock accounts after too many tries or blocking IPs with too many requests. 
  ```
    hydra -L usernames.txt -p 'funnel123#!#' {target_IP} ssh

    flags:
      -L : specify file with list of usernames
      -p : specify use only 1 password instead of a password list
      after the target IP we can specify the protocol for the attack
  ```
  Using hydra we find the username with the default password and ssh into their computer using those credentials. 

#### **Remote Machine Enumeration**
  A good command for finding files and services is <code>ss</code> which stands for *socket statistics*. 
  ```
    ss -tln
    
    flags:
      -l : display only listening sockets
      -t : display TCP sockets
      -n : do not try to resolve service names
  ```
  Running this command on the compromised machine we can see the following ports open:
  
  ![socket stats print](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Funnel/assets/socket_stats.png)

  First column indicates state the socket is in. *Recv-Q* displays number of queued received packets for that given port. *Send-Q* does so for sent packets. Fourth column shows local address and its port. The fifth column * and [::] indicate the port is listening on all interfaces meaning its externally accessible. Running <code>ss</code> without -n will show the services that is presumably running on the port. We can see that **

#### **Accessing Postgres**
  The typical way to access PostgreSQL is through CLI <code>psql</code>, however in this case, the user does not access the permissions to download the CLI. Potential walkarounds are to upload binaries onto the target machine, or bypass by port-forwarding using SSH

#### **Tunneling**
  To use local port forwarding with SSH: 
  ```
    ssh -L 1234:localhost:22 user@remote.example.com

    -L                      : local port forwarding
    1234                    : local port
    localhost               : remote host
    22                      : remote port
    user@remote.example.com : remote server
  ```
  This establishes a SSH client from the current machine to the remote server (user@remote.example.com). Then listen for incoming connection on the local port (1234). When a client connects to the local port (1234), the SSH client forwards connection to the remote server (22). This allows local client to access services on the remote server as if they were running on the local machine. 

  We want to forward traffic from *any* given local port (like port 1234), to the port with PostgreSQL (port 5432). To do this we specify it like this: 1234:localhost:5432. After executing this command:
  ```
    ssh -L {our_specified_port}:localhost:{target_port} {compromised_username}@{target_IP}
  ```
  Entering this command will respawn the shell and prompt for logging in again. This new SSH will have opened a socket on port 1234 and direct traffic toward port 5432. We can check using <code>ss</code>. 
  ![port_forward](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Funnel/assets/port_forward.png)
  Now we can use our installation of PostgreSQL to interact with the target machine. Run <code>psql</code> through port forwarding would look like: 
  ```
    psql -U christine -h localhost -p 1234
  ```
  Now that you have access to postgres through port forwarding and find the flag. 