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