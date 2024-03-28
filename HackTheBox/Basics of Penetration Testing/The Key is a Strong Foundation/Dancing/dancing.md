# Dancing

#### Difficulty: <code>Very Easy</code>

#### Machine Tags: protocols, SMB, reconnaissance, anonymous/guest access

#### Description
  > Finding shares on remote computers and exfiltrating by taking advantage of guest/anonymous access.  

#### Notes
  > #### **Server Message Block (SMB)** : Port 445
  > Protocol similar to FTP for sharing access to files, printers, serial ports between machines on a network. During scanning SMB is usually found on port 445. Runs on Application or Presentation layers, meaning it relies on other transport protols in the Transport layer. Microsoft SMB often uses NetBIOS over TCP/IP (NBT). 

  > Over SMB protocol files and other resources can be remotely accessed. An SMB-enabled storage on a network is called a <code>share</code>. This can be accessed by any client with the address of the server and credentials. Network admins can accidentally allow logins without valid credentials, guest accounts, or anonymous logons. 

  > #### **Enumeration**
  > <code>sudo nmap -sV {ip}</code>, -sV, determines service/version info. 
  > <code>smbclient</code> is a script that can help use to access a remote SMB share, if there is authentication required then it will prompt you for some. If no username is given, it defaults to your local username. 

  > #### **Foothold**
  > We can try to login to each of the shares using the format <code>smbclient \\\\{ip}\\{share}</code>.