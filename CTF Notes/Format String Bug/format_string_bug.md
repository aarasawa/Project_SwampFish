# Format String Bug

#### Intro
Format strings are control strings passed to printf() functions in C e.g. printf, sprintf, fprintf. The vulnerability emerges from unvalidated input into these functions by a user. Worse case, memory reads and writes can be performed. 

#### Format String Bugs
