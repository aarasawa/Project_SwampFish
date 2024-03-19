from pwn import *
import re

p = remote('titan.picoctf.net', 56491)

init = p.recv().strip().decode()
print(init)