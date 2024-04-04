# Sequel 

#### Difficulty: <code>Very Easy</code>

#### Machine Tags: vulnerability assessment, databases, mysql, sql, recon, weak credentials

#### Description
  Understanding structure of a database and learning how to traverse and gather information from a database. 

#### Notes
  #### **Enumeration**
  Scan the target and find that a port is open, running a service on port 3306. The service is named MySQL 5.5.5-10.3.27-MariaDB-0+deb10ul.

  #### **Foothold**
  To start we connect to the database using <code>mysql -h {IP} -u root</code>. The following commands are used in MySQL for navigating around a database:
  ``` MySQL
    SHOW databases;            :print db we have access to
    USE {db_name};             :set db to use by name
    SHOW tables;               :print available tables inside current db
    SELECT * FROM {table_name} :print all data from table_name
  ```
  We can use these to traverse the database and its table and retrieve the flag. 