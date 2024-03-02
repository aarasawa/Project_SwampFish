# Basic Injection - Easy

### Description: Use SQL injection to leak the database and capture the flag.

### 1. 
> The following link https://web.ctflearn.com/web4/ is provided which takes us to a page with a search box. 
> We can see that the query being submitted to the database follow: SELECT * FROM webfour.webfour where name = '$input'

### 2. 
> Initially, I was having trouble coming up with an approach to the problem. Since I overlooked how any input into the 
> search box gets into the SQL query already. The first couple minutes I was trying to input something like SELECT * FROM 
> webfour. Realizing I did not understand how to inject the query well enough, I searched through W3School. I then realized
> queries get put into the format **'$input'**. This mirrored the example in W3S where you can submit a query in the format 
> **something OR "" = "**.