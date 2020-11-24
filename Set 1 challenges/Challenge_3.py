# Single-byte XOR cipher
byte_str = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

def single_char_xor(input_bytes, value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ value])
    return output_bytes, value

for i in range(32, 128):
    print(single_char_xor(byte_str, i))

