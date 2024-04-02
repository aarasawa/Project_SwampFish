# SPG

#### Difficulty: <code>Very Easy</code>

#### Description
After successfully joining the academy, there is a process where you have to log in to eclass in order to access notes in each class and get the current updates for the ongoing prank labs. When you attempt to log in, though, your browser crashes, and all your files get encrypted. This is yet another prank for the newcomers. The only thing provided is the password generator script. Can you crack it, unlock your files, and log in to the spooky platform?

#### Program Overview
The program creates a string constant to be compared against during password generation. It includes all letters, digits, and some symbols. During the main function, a password is generated and then encrypted through a series of steps.

#### generate_password
The function appears to create a master key using the assignment below. It turns the *MASTER_KEY* byte string into an integer and specifies that the string is in little endian order. 
``` python
  master_key = int.from_bytes(MASTER_KEY, 'little')
```
It then loops over the *MASTER_KEY* integer, takes the bitmask against the binary representation for the integer of 1. Then based on whether its 0 or 1, it chooses between the front half or end half of the constant *ALPHABET* to append to the password. After, it right shifts the integer. 

#### Finding MASTER_KEY
The first step to decrypting the flag is finding MASTER_KEY. It is used for generating the encryption key and cipher for the flag. Our function, generate_masterkey should:  

&emsp;1. Receive the encrypted password as an argument  
&emsp;2. Turn the scrambled string back into the MASTER_KEY integer constant  
&emsp;3. Convert the integer constant back into a byte-string

To unscramble the password, we first recognize that taking the bitwise AND of the masterkey. It tells us that for every 1 and 0 bit, a 1 and 0, respectively, are appended onto the binary string. 

The thing that was tripping me up for a while is that when parsing the scrambled password. You need to do this in reverse since the scambling process starts from the LSB. If you are confused I did my best below to explain. 

``` python
  ''' DURING SCRAMBLING '''
  scrambled_password = ''
  binary string: 1010101010101010[1] <- LSB
    if bit is 1: randomly choose character in last half of ALPHABET
    else bit is 0: randomly choose character in front half of ALPHABET
  append character to scrambled_password
  right shift binary string: 101010101010101[0] <- new LSB
  # Hence characters are appended to the scrambled password in reverse order. 
```

#### Decrypting the Flag
Something that is easy to miss and stumped me during the process of decrypting the flag was this:
``` python
  b64encode(ciphertext.decode())
```

The flag was encoded in base64 before being printed. So the first thing to do in decrypting is to return it back into its ciphertext form pre-base64. Then:  
``` python
  '''
    1. Reproduce the cipher using AES
    2. Unpad and decrypt the ciphertext using everything we acquired
    3. Decode plainetext back into a string
  '''
  1. cipher = AES.new(encryption_key, AES.MODE_ECB)
  2. plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
  3. plaintext.decode('utf-8')
```