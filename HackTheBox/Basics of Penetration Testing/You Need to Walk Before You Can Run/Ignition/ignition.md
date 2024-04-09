# Ignition

#### Difficulty: <code>Very Easy</code>

#### Machine Tags:
  Common Applications  
  Magneto  
  Reconnaissance  
  Website Structure Discovery  
  Weak Credentials  

#### Description
  Enumerate the target, find the hidden page, login, and find the flag. 
  
#### **Enumeration**
  Scanning shows that a ngix 1.14.2 is open on port 80. Indicating that a website might be running on the target. Trying to access the link renders no result. However there is a link change hinting at virtual hosting. To get a better view of request interactions, we can use <code>curl</code>.  
  ```
    curl -v http://{IP}/
  ```
  We can try to access something by adding the IP to our /etc/hosts. 

#### **Gobuster**
  We can search for hidden or other pages using gobuster. Initiating a gobuster we can find several pages including an admin page. Appending /admin to the end of the URL gives us a login page. 

#### **Magento**
  According to documentation, we can see multiple layers of security to prevent unauthorized access. Initial sign-ons are required to setup 2FA. Additionally, brute-force is out of the question since it has bruteforce measures. We can try to guess. Magento passwords must have:   
    &emsp;1. Must be at least 7 characters long  
    &emsp;2. Must have 1 alpghabetic and 1 numeric character  
  We can lookup the most common passwords to try and guess according to the password requirements: 
  https://cybernews.com/best-password-managers/most-common-passwords/
    &emsp;1. qwerty123
  Oh first try worked. 
