# Delulu

#### Difficulty: <code>Very Easy</code>

#### Description
> HALT! Recognition protocol initiated. Please present your face for scanning.

#### 1. 
> For this challenge, I learned about string formatting vulnerabilities in C, and working with <code>checksec</code> as a tool for analyzing the properties of Executable and Linkable Format binaries (ELF). Running <code>pwn checksec delulu</code> in terminal, presents us with: 

```  
Arch:    amd64-64-little
RELRO:   Full RELRO
Stack:   Canary found
NX:      NX enabled
PIE:     PIE enabled
RUNPATH: b'./glibc/'
```

#### 2. 
<ol>
    <li>Full RELRO (Relocation Read-Only) indicates that all relocation sections in the binary are read only to prevent types of overwrite attacks like buffer overflow. </li>
    <li>Stack canaries are used to detect stack buffer overflows, they are values placed on the stack before the return address and being modified indicates a potential exploit attempt.</li>
    <li>NX (No eXecute) enabled means the binary has Data Execution Prevention (DEP) or equivalent to prevent executing code from memory regions marked as data. This prevents exploit techniques like injecting shellcode into data buffers.</li>
    <li>PIE (Position Independent Executable) enabled indicates the binary is compiled to be loaded at random address in memory, making it difficult for attackers to predict memory addresses.</li>
</ol>