# Simple BOF

#### Difficulty: <code>Easy</code>

#### Description
> Want to learn the hacker's secret? Try to smash this buffer!

#### 1. 
> The program has a really cool visualization. Before I did not really understand what the point of buffer overflow was, I understood you can input things to overflow the buffer. However, not really understanding how to get what you want from doing it. Analyzing the program, I realized that the hex value represents the ascii value for "flag" then overflowing it with the string returned the flag. 

![image of the buffer visualization and my buffer overflow](simple_bof.png "Simple Buffer Overflow")