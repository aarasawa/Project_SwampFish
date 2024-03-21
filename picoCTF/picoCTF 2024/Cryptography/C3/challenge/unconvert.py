import sys

chars = ''

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

f = open('ciphertext', 'r')
ciphertext = f.read().strip()

plaintext = ''

prev = 0
for char in ciphertext:
  cur = lookup2.index(char)
  plaintext += lookup1[(cur + prev) % 40]
  prev = (cur + prev) % 40 

chars = ""

for line in ciphertext:
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print(chars[i]) #prints
        b += 1 / 1