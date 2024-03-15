# Character - Very Easy

### Description
> Security through induced Boredom is a personal favorite approach of mine. Not as exciting as 
> something like The Fray, but I love mkaing it as tedious as possible to see my secrets, so you can
> only get one character at a time!

### 1.
> Accessing the target ip using netcat produces a prompt allowing for input of the index for the flag.
> So I thought about writing a script to input numbers as the flag would probably be long. 
> I piped a .txt with numbers from 1 to 100 into the netcat prompt and received answers and did not 
> reach the end of the flag yet! There is probably a better way to do this, but seeing as I have not
> written Python scripts for interacting with netcat servers its going to be a bit clunky at first. 

### 2. 
> All that is left is to parse, the flag was 103 characters long. I piped the output from the netcat
> server interactions in another .txt and parsed the results. Returning and concatenating the last
> characters from each line together and got the flag. 