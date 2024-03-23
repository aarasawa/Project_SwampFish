# Format String Bug

#### Intro
Format strings are control strings passed to printf() functions in C e.g. printf, sprintf, fprintf. The vulnerability emerges from unvalidated input into these functions by a user. Worse case, memory reads and writes can be performed. 

#### Format String Bugs
In C, <b>variadic function</b> are declared with the list of arguments ending in '...'. The first part of the function is the only part that is validated. On 64-but systems, the first 6 arguments are passed in registers and additional arguments are pushed onto the stack. 

In the second line, each '%' character is interpreted as a format specifier. If there are no corresponding arguments in the function, <code>printf</code> will read the registers or memory locations of arguments.

``` C
 int printf(const char *fmt, ...);
 printf(buf);

 //correct way to print a string
 puts(buf);
 printf("%s", buf);
```

#### Exploiting Format String Bugs
<code>printf()</code> can also write to memory. An instruction pointer sees character as an instruction to print the character. For printf(), the machine interprets each character as an "operation" so the instruction pointer moves past the character in the string and the output counter is incremented by one. 

``` C
1 a <---- instruction ptr
2 b
3 c
4 d
```

#### Stack Reads
On 32-bit systems, a series of '%x' specifiers in printf() causes it to print successive lines from the stack. On 64-bit systems, the first 5 '%lx' will print contents from <b>rsi, rdx, rcx, r8, r9</b> registers, additional '%lx' will start printing successive stack lines. 

32-bit systems using <b>%x</b>: can read canary
64-bit systems using <b>%lx</b>: read canary, using '%x' will only read 4 bytes

The difficulty lies in the fact that argument pointers only moves forward by 1 froma format specifier. 

#### Random Access to Arguments
Format string can access its arguments in random order using <code>%n$</code> to the select the <i>nth</i> argument. For example, if we know the canary is <i>n</i> stack-lines below ptr to format string then a format specifier like 
<code>“%n$x”</code> prints the canary on 32-bit systems and <code>%(n + 5)$lx</code> does the same for 64-bit systems.

``` C
  printf("%4$d %1$d %3$d %2$d\n", 10, 20, 30, 40);
```

