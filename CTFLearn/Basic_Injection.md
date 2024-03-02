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

### 3. 
> The basics for why **something OR "" = "** is needed is because the format in the example returns a query for its database
> as: **SELECT * FROM users WHERE Name="John Doe" AND Pass="myPass"** where "John Doe" and "myPass" are inputs from the user. 
> Hence an input like **" or "" = "** would be queried on the database like **SELECT * FROM users WHERE Name="" or "" = "" ...**.
> Looking to the query stucture of the site provided, we can see they used single quotes instead of double quotes.

#### Solution
> **' OR '' = '**. A small explanation about why this works is contained in the **OR '' = '**. Because the query completes to 
> **'' OR '' = ''**, the latter part of the query will always evaluate to TRUE. Allowing us to view the contents for the entire table.