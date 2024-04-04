# Appointment

#### Difficulty: <code>Very Easy</code>

#### Machine Tags: databases, apache, mariadb, php, sql, recon, sql injection

#### Description
  > Learn to get familiar with the enumeration process and teach how to perform simple SQL injection.

#### Notes
  #### **Enumeration**
  Perform an nmap scan to determin open ports on the target. A new flag is being used to specify to look at the 1000 most common TCP ports. We see that its running Apache 2.4.38, which is an open-source application that runs web pages on physical or virtual web servers. Popular HTTP ports are 80, 443, 8080, 8000 TCP. Web admin need to make sure directories with sensitive info are seured so users cannot manually navigate to them. To find hidden pages, using a directory buster is useful.

  #### **Gobuster**
  For finding info on commands we can use:
  ``` 
    gobuster --help
  ```
  Parrot OS has pre-installed wordlists that we can use for this. A command for directory busting using a wordlist would look like this:
  ```
    gobuster dir --url http://{IP}/ --wordlist {wordlist_location}/{wordlist_file}
  ```
  Returns nothing useful when trying to enumerate directories on the target IP. 

  #### **What Next?**
  We still have not tried to login to the application using default or easy to guess credentials. Things like username: admin, password: admin. 

  #### **SQL Injection**
  SQL injection takes advantage of vulnerable applications with little or no protections in validating user input. A user can take advantage of this to bypass logins, view sensitive information from the database, drop a table, etc. 

  #### **Specific SQL Injection PHP**
  The type of injection they carried out worked well in this instance because they knew the type of language they were working with and how the program was written. It took advantage of commenting in PHP where the username <code>admin '#</code> was used. The single quote closed the input for the username, and the hashtag commented out the input for the password. So when the inputs are parameterized into the query, only the username is used, what would be the rest of the query after the input username is commented out. To illustrate:
  ``` php
    # Given a parameterized query like this
    $sql="SELECT * FROM users WHERE username='$username' AND password='$password'";

    # An injection of "admin '#" would give
    $sql="SELECT * FROM users WHERE username='admin '#' AND password='$password'";
  ```
  The program also only validates a login search by looking to see if only 1 row has been returned by a query. All you need to login is the particular username and any string would suffice for the password since it is not used at all. 