# Basic Injection 

### Description: Use SQL injection to leak the database and capture the flag.

### 1. 
> The following link https://web.ctflearn.com/web4/ is provided which takes us to a page with a search box. 
> We can see that the query being submitted to the database follow: SELECT * FROM webfour.webfour where name = '$input'

### 2. 
> Initially, I was having trouble coming up with an approach to the problem. Since I overlooked how any input into the 
> search box gets into the SQL query already. The first couple minutes I was trying to input something like SELECT * FROM 
> webfour. 