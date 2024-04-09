# Tactics

#### Difficulty:<code>Very Easy</code>

#### Machine Tags:
  Protocols  
  SMB  
  Reconnaissance  
  Misconfiguration  

#### Description
  Learning about Windows misconfigurations and taking exploiting it in two different ways. 

#### **Initial Enumeration**
  Trying to ping the target with several normal flags such as -sC and -sV yields no result. If we assume this to be the firewall, a typical scans are bound to set off detectors. Using the <code>-Pn</code> flag skips the host discovery phase and goes to other probes, silencing active scanning to some degree. 

  135/tcp msrpc
  139/tcp netbios-ssn
  445/tcp microsoft-ds

#### **General Port Information**
  **Port 135** : Remote Procedure Call (RPC) supports communication between Windows applications. A low-level form of inter-process communication where a client process can make requests of a server process. 

  **Port 139** : NetBIOS is an acronym for Network Basic Input/Output System. On the session layer of OSI  for applications on separate computers to communicate over LAN. Modern networks have NetBIOS run over TCP/IP, NetBIOS is also used for identifying system names in TCP/IP. 

  **Port 445** : Server Message Block (SMB) is a network file sharing protocol that requires an open port on a computer or server to communicate with other systems. Port numbers for SMB are typically *139* and *445*. *Port 139* is used by SMB  dialects that communicate over NetBIOS. A session layer protocol designed to use in Windows OS over a local network. *Port 445* used by newer SMB versions over TCP stack, allowing communication over the Internet. 

#### **SMB Access**
  SMB is a file sharing protocol so it is possible to extract some resources. This can be done using a utility called <code>smbclient</code>.
  ```
    smbclient -L {target_IP} -U Administrator

      -L : list available shares on target
      -U : login identity to use
  ```
  To sign in we can hope that the default credentials still work or there is no password. 
  ![login to smb](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Tactics/assets/login_smbv.png)
  As we can see there are multiple shares.

#### **Options, Options**
  From here we have two options:  
    &emsp;1. Navigate to C$ share with admin permissions   
    &emsp;2. Use PSexec.py from Impacket with installation and common attack surface, big fingerprinting  
  *Navigate to C$ share with Admin permissions*
  ```
    smbclient \\\\\{IP}\\C$ -U Administrator
  ```
  *Impacket*
  To access <code>ADMIN$</code> we can use <code>psexec.py</code> to exploit misconfigurations to get the interactive shell. The script *psexec.py* is part of the Impacket framework. 
  
#### **Impacket** 
  *Impacket* is a Python framework for working with network protocols to provide low-level access to packets for protocols like SMB and MSRPC. *PsExec* is a tool from Microsoft that lets you run processes remotely from using any user's credentials. This can create a remote service by uploading a randomly-named executable on the <code>ADMIN$</code> share on the remote system and register it as the Windows service. Allowing us access to an interactive shell on the remote system over TCP. 

  The command for getting an interactive shell from a target:
  ```
    python psexec.py username:password@hostIP
  ```
  ![impacket login](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Tactics/assets/impacket_login.png)

  We now have a shell with the highest permissions. However using <code>pkexec</code> is often preferred in simulated testing environments but can be detected by Windows Defender. 