# Pennyworth

#### Difficulty:<code>Very Easy</code>

#### Machine Tags:
  Common Applications  
  Jenkins  
  Java  
  Reconnaissance  
  Remote Code Execution  
  Default Credentials  

#### Description
  Explore arbitrary code execution (ACE).

#### **Arbitrary Code Execution**
  To identify, define, and catalog publicly disclosed vulnerabilities is called *CVE* or Common Vulnerabilities and Exposures. The ability to execute arbitrary commands or code on a target machine or in a target process. Ability to trigger ACE over a network is often called *remote code execution* (RCE). 

#### **Initial Enumeration**
  8080/tcp    http    Jetty 9.4.39.v20210325

#### **Jenkins**
  The server we visit is running Jenkins, doing some initial research can tell us a bit about this service. *Jenkins* is a free and open-source server to automate parts of software development. Server-based system. 

  We are presented with a login screen, so the simplest thing to do right now would be to look online for default credentials for Jenkins. Working down the list we eventually find a correct pair. 

  For connecting, we are going to try a reverse shell connection using Groovy commands. 