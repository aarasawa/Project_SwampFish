# Delulu

#### Difficulty: <code>Very Easy</code>

#### Description
> HALT! Recognition protocol initiated. Please present your face for scanning.

#### 1. 
> I do not have more time to take more cracks at these problems so I will just review the writeups and learn how to use the technologies and methods. For this challenge, I learned about string formatting vulnerabilities in C, and working with <code>checksec</code> as a tool for analyzing the properties of Executable and Linkable Format binaries (ELF). Running <code>pwn checksec delulu</code> in terminal, presents us with: 

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

#### 3. 
> Next, the format string bug exploits the consequence of insecure string formatting in C. When the input from a user to used directly to print using methods like printf, sprintf, fprintf, etc. Without validation, users can inject formatting specifying options like seen below. 

```
  The D-LuLu face identification robot will scan you shortly!

  Try to deceive it by changing your ID.

  >> %p %p

  [!] Checking.. 0x7ffd4bd5b7d0 (nil)

  [-] ALERT ALERT ALERT ALERT
```

#### 4. 
> Disassembly is the next step, from what I can glean in the writeup this would mean disassembling the ELF to understand the code and what functions are being called. Writing a couple of format specifiers to the executable will write out the stack addresses. The trickiest part is the disassembly, I need to brush up on my assembly because I do not know how the author got from the objdump to readable C code. 

#### 5. 
> I understand the concept, just need to polish my disassembly skills. 