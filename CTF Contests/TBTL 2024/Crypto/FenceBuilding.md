# Fence Building

#### Description
I've recently got into woodworking and have build a beautiful fence just like this one (shows a picture of a split rail fence). Now I'm working on a flag, but it turns out all garbled for some reason. {flag}

#### Rail Fence Cipher
I had to dig around a bit. However the big hint was the rail fence. It led me to the rail fence cipher, a *transposition cipher* that creates up-down diagonals from left to right using the plaintext. The ciphertext is created by following the rows created along these diagonals from left to right, starting from the first row to the last depending on the number of rows, i.e. *rails* you want. 

Example:
``` python
  rails = 4, offset 0, plaintext = FLAG{THIS_IS_FAKE}
  rail 1: F          H         _
  rail 2:   L      T   I     S   F      }
  rail 3:     A  {      S   I     A   E
  rail 4:       G         _         K

  # To generate the ciphertext
  ciphertext = ''
  for rail_num in range(rails):
    append letters in rail_num in order. 
  ciphertext = FH_LTISF}A{SIAEG_K
```

#### Solution
The flag is all garbled however, it has all the elements that a flag would have like braces. So I am guessing it just mixed using some kind of cipher and it is not converted to some other number base. This led me to search any kind of ciphers (i.e. fence or rail ciphers based on the hint). 