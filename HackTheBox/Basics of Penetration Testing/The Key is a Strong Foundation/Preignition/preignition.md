# Preignition

#### Difficulty: <code>Very Easy</code>

#### Machine Tags: custom applications, apache, recon, website structure discovery, default credentials

#### Description
  > Room for learning how to use Gobuster for directory busting. Including concept of directory busting and what a tool for this purpose does to find hidden pages. 

#### Notes
  > #### **Enumeration**
  > Use nmap to scan for open ports on the target IP. Seeing that the port open is an http port, I tried to plug in the IP on a web browser to see if it was a website. It seems to be the default nginx page for new web servers. 

  > #### **Gobuster**
  > The new tool for this machine is Gobuster, its a tool for directory busting. In this case, I assume we are going to use it to search for hidden pages on the IP. It has a wordlist to search through with common page names and you can specify page extensions as well. Instead of brute-forcing through typing the path on a browser, it directly sends GET requests to the web server. 

  > #### **Foothold**
  > Default credentials worked to login to the admin page that was found using Gobuster. 