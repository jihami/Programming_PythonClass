with open("binary_to_text.bin","wb") as f:
    ga = b"\xea\xb0\x80" #1바이트 씩 3개를 써으니 3바이트
    f.write(ga)
with open("binary_to_text.bin", "r", encoding="utf-8") as f:
    data = f.read()
print(data)