# Crocodile

#### Difficulty:<code>Very Easy</code>

#### Machine Tags
  custom applications  
  protocols  
  apache  
  ftp  
  recon  
  website structure discovery   
  clear text credentials  
  anon/guest access  

#### Description
  Revisit insecure access configurations on FTP and an administrative login for a website. 

#### **Enumeration**
  Scan show that port 21 is open. The service is FTP, version: vsftpd 3.0.3. Port 80 is also open. Running apache httpd 2.4.41 ((Ubuntu)). 

#### **Login**
  Then I see if I can login using guest or anonymous credentials. Using 'anonymous' login is allowed. Additionally, listing the files and directories available reveals two listings: allowed.userlist, allowed.userlist.passwd.

#### **Wappalyzer**
  Wappalyzer is a browser plug-in that analyzes the webpage's code and returns the technologies that made it. Using it to analyze the webapp we find: 
  ```
    Misc:        Popper                     JS libraries:  jQuery, Modernizr, Slick, Isotope
    Web Servers: Apache                     UI frameworks: bootstrap
    OS:          Ubuntu                     Languages:     PHP
    Maps:        Google Maps
  ```

#### **Gobuster**
  Manually trying to navigate around the webapp yielded nothing. So we can try to use gobuster to find any pages. Now that we know the site is using PHP we can specify an extension to look for. 
  ``` 
    To specify using a file extension in a gobuster cmd:
    gobuster dir --url {URL} --wordlist {filepath_wordlist} -x {extensions}
  ```
  We find a hidden login page to use. 

#### **Logging In**
  Finally we can use the credentials that are kept in the FTP server to login to the hidden page. 