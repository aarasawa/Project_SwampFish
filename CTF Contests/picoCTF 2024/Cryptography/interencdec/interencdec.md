# interencdec

#### Tags: Cryptography, base64, browser_webshell_solvable, caesar

#### Description
> Can you get the real meaning of this file

#### 1. 
> The encoded file provides a string that seems to be encoded in base64. So I decode it, which yields another subsequent string that indicates to be a byte string representation. I remove the outer part of the bytestring representation and decode it again because it is in base64 encoding still. This yields text in the form of a flag. Based on the tag for the challenge and the format for the string, running this through a caesar cipher will yield the flag. 