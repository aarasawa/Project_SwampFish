import base64

flag = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"

b_flag = base64.b64decode(flag)

s_flag = b_flag.decode('utf-8')

print(s_flag)