import base64

enc_flag = 'cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMjgzZTYyZmV9'

dec_str = base64.b64decode(enc_flag).decode('utf-8')

print(dec_str)