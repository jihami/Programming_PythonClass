print("전체 한꺼번에 읽기")
f = open("text.txt", "r", encoding="utf-8")
data = f.read()
f.close()
print(data)
print("한줄씩 읽기")
f = open("text.txt", "r", encoding="utf-8")
line = f.readline() #line : 다빈보라\n 이 들어 잇음 -> textㅎ파일에 있는거임
print(line)
line = f.readline()
print(line)

while True:
    line = f.read() #line : 다빈보라\n
    if line == "" : #빈칸이라면 끝나라
               break
    print(line)
f.close()