import base64

f = open('enc_flag', 'r')
enc_flag = f.read().strip()

x = base64.b64decode(enc_flag).strip()

byte_string = b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ=='
cipher = base64.b64decode(byte_string).decode('utf-8')

def caesar(ciphertext):
  plaintext = ''
  for rot in range(0, 27):
    for char in ciphertext:
      if 'A' <= char <= 'Z':
        plaintext += chr((ord(char) - ord('A') + rot) % 26 + ord('A'))
      elif 'a' <= char <= 'z':
        plaintext += chr((ord(char) - ord('a') + rot) % 26 + ord('a'))
      else:
        plaintext += char
    print(plaintext)
    plaintext = ''

caesar(cipher)