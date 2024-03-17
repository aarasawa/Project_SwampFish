# Writing on the Wall 

#### Difficulty: <code>Very Easy</code>

#### Description
> As you approach a password-protected door, a sense of uncertainty envelops you—no clues, no hints. Yet, just as confusion takes hold, your gaze locks onto cryptic markings adorning the nearby wall. Could this be the elusive password, waiting to unveil the door's secrets?

#### 1. 
> Running checksec on the the executable returns that all protections are enabled on the file. Writing to the terminal does not indicate any string formatting or buffer overflow vulnerability. This problem revolves around the null byte vulnerability with the strcmp method in C. 