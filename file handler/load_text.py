print("전체 한꺼번에 읽기")
f = open("text.txt", "r", encoding="utf-8")
data = f.read()
f.close()
print(data)
print("한줄씩 읽기")
f = open("text.txt", "r", encoding="utf-8")
line = f.readline()
f.close()
print(line)