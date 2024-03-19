# Basics

#### ASCII
> 7-bit encoding to represent text using integers between 0-127. 

``` python
  chr() # convert ASCII number representation to character
  ord() # convert character into num representation
```

#### Hexadecimal 
> Base-16 number system, often used for encoding ASCII strings.

``` python
  bytes.fromhex() # convert hex to bytes
  something.hex() # convert byte strings to hexadecimal
  int(x, 16)      # can also use int() method and specify base number system as second arg 
```

#### Base64
> Base-64 commonly used online for binary data in images for HTML/CSS files

``` python
import base64

  base64.b64encode() #encode a string 

```

#### Bytes and Big Integers
> Common way to convert characters into ordinal bytes of the message is to convert to hex and concatenate. Basically the flow is characters -> ascii bytes -> hex bytes (base16)

``` python
#using pycryptodome library
from Crypto.Util.number import *

  bytes_to_long() # convert byte string into long integer
  long_to_bytes() # inverse operation of the above method
```

#### XOR Starter
> 