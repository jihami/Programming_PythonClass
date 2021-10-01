print("전체 한꺼번에 읽기")
f = open("text.txt", "r", encoding="utf-8")
data = f.read()
f.close()
print(data)


with open("text.txt", "r", encoding="utf-8"):
    data = f.read()
print(data)


print("한줄씩 읽기")
f = open("text.txt", "r", encoding="utf-8")
# line = f.readline() #line : 다빈보라\n 이 들어 잇음 -> textㅎ파일에 있는거임
# print(line)
# line = f.readline()
# print(line)

while True:
    line = f.read() #line : 다빈보라 \n
    if line == "" : #빈칸이라면 끝나라
        break
    print(line.rstrip()) #line.replace("\n","")
f.close()

print("전체를 한꺼번에 읽고, 줄 별로 리스트")
f = open("text.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
for line in lines:
    print(line.rstrip())

#quiz
#이름 : 다빈[tab] 좋아하는 색:보라
#이름 : 다빈[tab] 좋아하는 색:보라
f = open("text.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
for line in lines:
    #크리스찬:"검정색"
    data = line.split(":") #["고에스터","검은색"]
    # print("이름 : "+line.rstrip()[:3]+ "\t 좋아하는 색 : "+line.rstrip()[4:] )
    print("이름 : "+data[0].rstrip() +  "\t 좋아하는 색 : "+data[1].rstrip())