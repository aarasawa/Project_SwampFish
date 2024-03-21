'''
encrpytion process:
  

'''
def generator(g, x, p):
    return pow(g, x) % p

def decrypt(encrypted, key):
    cipher = ''
    for char in encrypted:
        decrypted_ord = char // (key * 311)
        cipher += chr(decrypted_ord)
    return cipher

def dynamic_xor_decrypt(ciphertext, text_key):
    plaintext = ""
    key_length = len(text_key)
    for i, char in enumerate(ciphertext):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))  # Perform XOR again
        plaintext += decrypted_char
    return plaintext

if __name__ == '__main__':
  text_key = "trudeau"

  a = 89
  b = 27
  p = 97
  g = 31
  
  cipher = [33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104, 156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732, 231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332, 119424, 182868, 97032, 26124, 44784, 63444]
  
  u = generator(g, a, p)
  v = generator(g, b, p)
  key = generator(v, a, p)
  b_key = generator(u, b, p)
  shared_key = None
  if key == b_key:
      shared_key = key
  ciphertext = decrypt(cipher, shared_key)

  plaintext = dynamic_xor_decrypt(ciphertext, text_key)
  print(plaintext[::-1])