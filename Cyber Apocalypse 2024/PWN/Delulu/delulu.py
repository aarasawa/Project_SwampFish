from pwn import checksec

bin_path = './glibc/'

print(checksec(bin_path))