with open("text.bin","wb") as f:
    f.write(b"\xea\xb0\x80")
input()
with open("binary.bin", "rb") as f:
    data = f.read()
print(data) #b"\xff\x00\x7f": 111111110000000001111111    \x -> 16진수하는 뜻