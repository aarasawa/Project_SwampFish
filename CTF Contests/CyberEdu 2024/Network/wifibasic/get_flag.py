
from hashlib import sha256

BSSID = "02:00:00:00:00:00"
ESSID = "BitSentinelRulez"
PSK = ""

def calculate_sha256(bssid, essid, psk):
    input_string = bssid + essid + psk
    hash_result = sha256(input_string.encode()).hexdigest()
    return hash_result

sha256_sum = calculate_sha256(BSSID, ESSID, PSK)
print('CTF{'+sha256_sum+'}')