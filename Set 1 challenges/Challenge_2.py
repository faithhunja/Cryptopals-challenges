# Fixed XOR
def fixed_xor(str1, str2):
    byte_str1 = bytes.fromhex(str1)
    byte_str2 = bytes.fromhex(str2)
    print((bytes([b1 ^ b2 for b1,b2 in zip(byte_str1, byte_str2)])).hex())

fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')