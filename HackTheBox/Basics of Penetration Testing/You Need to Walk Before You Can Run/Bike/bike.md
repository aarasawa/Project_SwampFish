# Bike

#### Difficulty:<code>Very Easy</code>

#### Machine Tags:
  Custom Applications  
  NodeJS  
  Reconnaissance  
  Remote Code Execution  
  Server Side Template Injection (SSTI)  

#### Description
  Learn of Server-Side Template Injection on Handlebars, a template engine in NodeJS.

#### **Enumeration**
  Two ports are open:  
    &emsp;22/tcp : OpenSSH 8.2p1 Ubuntu 4ubuntu0.4  
    &emsp;80/tcp : Node.js (Express middleware) Bike
  ```
  Web Frameworks:        Express                    CDN:                  Google Hosted Libraries
  Web Servers:           Express                    JavaScript libraries: jQuery
  Programming Languages: Node.js
  ```

#### **Technologies**
  **Node.js** is a backend-end JavaScript runtime environment that can be used to build scalable network applications
  **Express** Node.js web application framework that provides a robust set of features for web and mobile applications

  **Template Engine** are used to display dynamically generated content on a webpage. Variables inside a template file are replaced by actual values. 

  **SSTI** or server-side template injection is a vulnerability where malicious input is inserted into a template in order to execute commands on the server. Native code is injected into the webpage, the code is then run by the template engine and the attacker can execute code on the affected server. 


#### **Testing the Waters**
  We can input a test email into the webpage to see what happens. It appears to take the email and print it to the screen hinting that we could possible to some Cross Site Scripting (XSS). Testing it with other strings like scripts are not working so XSS may not be a good approach. 

  Node.js and Python web backend servers often make use of a software called *Template Engines*

#### **Identification**
  To confirm the existence of the vulnerability on the webpage, there are resources online that can help us to identify the engine that is being used. Common special characters in template expressions are: 
    &emsp;{{7*7}}
    &emsp;${7*7}
    &emsp;<%= 7*7 %>
  Submitting payloads of these types can be used to identify SSTI since the potential for the web server to excute the code will return 49 instead of the string. Attempting some of the payloads causes the application to throw an error. From the error page, we are able to see that the server is running from <code>/root/Backend</code> and that <code>Handlebars</code> template engine is being used. 

#### **Exploitation**
  BurpSuite can be used to edit the packets that we send to the web server. Here: https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection. We can have the server execute different system commands on the server. 

#### **URL Encoding**
  In a request to a web server, data can only be sent from the ASCII character set. So then we can use <code>decoder</code> to decode or encode text using various encoding methods. Sending this under the <code>email</code> parameter in the HTTP request, we get an error response in return <code>require is not defined</code>. 

  <code>require</code> is a keyword in JavaScript and Node.js to load code from other modules or files. Our payload tries to load from the child process module into memory to execute system commands. 

#### **Globals**
  __dirname, __filename, exports, module, require() are global objects in Node.js. Since <code>require</code> is not in the global scope and could be inaccessible in some cases. There is a <code>process</code> object available which gives info and control over current Node.js process. Resending the modified payload we get:

  ![modified payload result](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Bike/assets/Screenshot%202024-04-06%20002329.png)

  Since the process object is available, one thing to check is to see if mainModule is also available. After modifying the payload again <code>process.mainModule</code>, no error is thrown is a good sign. From here let's attempt to use require through this method and load a child process. Remodifying and resending yields no erorr. We continue. This time we can try to execute <code>whoami</code>.

  ![execSync payload](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Bike/assets/execSync_payload.png)

  From resending with a whoami command included we see that it was executed by root. This indicates that we can run system commands. Now that we know we can execute commands, we can try to check the situation of the directory by sending <code>ls /root</code> We get:

  ![ls cmd](/HackTheBox/Basics%20of%20Penetration%20Testing/You%20Need%20to%20Walk%20Before%20You%20Can%20Run/Bike/assets/ls_cmd.png)

  From here can just run <code>cat /root/flag.txt</code>. 