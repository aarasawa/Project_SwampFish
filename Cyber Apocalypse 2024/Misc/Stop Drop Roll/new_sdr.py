from pwn import *

p = remote('94.237.63.128', 48219)

p.sendlineafter(b'(y/n) ', b'y')
p.recvline()

while True:
    recv = p.recvlineS().strip()

    if 'GORGE' not in recv and 'PHREAK' not in recv and 'FIRE' not in recv:
        print(recv)
        break

    result = recv.replace(", ", "-")
    result = result.replace("GORGE", "STOP")
    result = result.replace("PHREAK", "DROP")
    result = result.replace("FIRE", "ROLL")

    p.sendlineafter(b'do? ', result.encode())