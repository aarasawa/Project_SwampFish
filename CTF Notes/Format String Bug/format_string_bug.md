# Format String Bug

#### Intro
Format strings are control strings passed to printf() functions in C e.g. printf, sprintf, fprintf. The vulnerability emerges from unvalidated input into these functions by a user. Worse case, memory reads and writes can be performed. 

#### Format String Bugs
In C, <b>variadic function</b> are declared with the list of arguments ending in '...'. The first part of the function is the only part that is validated. 

``` C
 int printf(const char *fmt, ...);
```