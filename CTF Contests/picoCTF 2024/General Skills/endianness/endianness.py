import struct

def string_to_endians(s):
    # Convert string to bytes
    byte_str = s.encode('utf-8')

    print(''.join(format(b, '02x') for b in byte_str[::-1]))

    # Little-endian representation
    little_endian = ':'.join(format(b, '02x') for b in byte_str[::-1])

    print(''.join(format(b, '02x') for b in byte_str))

    # Big-endian representation
    big_endian = ':'.join(format(b, '02x') for b in byte_str)

    return little_endian, big_endian

# Example usage
input_string = "rrfxy"
little_endian, big_endian = string_to_endians(input_string)
print("Little-endian:", little_endian)
print("Big-endian:", big_endian)