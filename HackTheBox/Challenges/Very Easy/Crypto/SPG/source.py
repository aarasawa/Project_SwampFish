from hashlib import sha256
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

ENCRYPTED_PASSWORD = 't*!zGnf#LKO~drVQc@n%oFFZyvhvGZq8zbfXKvE1#*R%uh*$M6c$zrxWedrAENFJB7xz0ps4zh94EwZOnVT9&h'
ENCRYPTED_FLAG = b'GKLlVVw9uz/QzqKiBPAvdLA+QyRqyctsPJ/tx8Ac2hIUl8/kJaEvHthHUuwFDRCs'

def generate_masterkey(password: str) -> bytes:
    bitstring = ''

    for char in password[::-1]:
        if char in ALPHABET[:len(ALPHABET)//2]:
            bitstring += '1'
        else:
            bitstring += '0'

    master_key = int(bitstring, 2)
    return master_key.to_bytes((master_key.bit_length() + 7) // 8, 'little')

def main():
    master_key = generate_masterkey(ENCRYPTED_PASSWORD)
    encryption_key = sha256(master_key).digest()
    ciphertext = b64decode(ENCRYPTED_FLAG)
    cipher = AES.new(encryption_key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print(plaintext.decode('utf-8'))
    
if __name__ == '__main__':
    main()
