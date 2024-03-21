hex_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
key = "crypto"

def main():
    # convert into byte string from hex
    bytes_data = bytes.fromhex(hex_string)
    bytes_key = key.encode('utf-8')
    xored_bytes = bytes([byte ^ bytes_key for byte in bytes_data])
    print(xored_bytes)

if __name__ == "__main__":
    main()