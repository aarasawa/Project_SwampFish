# Explosion

#### Difficulty: <code>Very Easy</code>

#### Machine Tags: programming, rdp, recon, weak credentials

#### Description
  > For me, was a refersher on CLIs and GUIs.

#### Notes
  > #### **CLI - Remote Access Tools**
  > RDP runs on ports 3389 TCP and UDP. Telnet is unencrypted so it has become deprecated and replaced by SSH. Both Telnet and SSH are remote terminal tools so you would need another tool to view the display like <code>xfreerdp</code>. 

  > #### **GUI - Remote Access Tools**
  > Prevalent Remote Desktop tools are TeamViewer and Windows Remote Desktop Connection. Software that runs natively can sometimes be misconfigured. 

  > #### **Enumeration**
  > Using nmap to identify open ports we see that port 3389 is open for Microsoft Terminal Services. It is typically used for Remote Desktop and Remote Assistance connections. We can then check to see if it is misconfigured. 

  > #### **Foothold**
  > We can try to use different guest logins to access the system. Usually I would try for admin accounts first, as in a lot of systems many do not reconfigure the default admin login.  