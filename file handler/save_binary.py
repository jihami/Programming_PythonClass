with open("binary.bin", "wb") as f:
    byte_list = bytes([255, 0, 127]) #111111110000000000001111
    f.write(byte_list)