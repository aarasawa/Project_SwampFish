string = 'label'
num = 13

new_string = [ord(x) ^ num for x in string]

print(''.join(chr(x) for x in new_string))