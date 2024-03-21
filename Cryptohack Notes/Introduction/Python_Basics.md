#### Convert byte string from hex
``` python
  bytes_data = bytes.fromhex(hex_string)
```

#### Convert a string into byte string
``` python
  bytes_data = string.encode('utf-8')
```

#### Decode the bytes to ASCII
``` python
  ascii_string = byte_data.decode('utf-8')
```

#### Perform XOR byte by byte
``` python
  xored_bytes = bytes([a ^ b for a, b in zip(bytes_data, string_bytes)])
```