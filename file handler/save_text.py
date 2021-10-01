f = open("text.txt","w", encoding="UTF-8")
f.write("다빈")
f.write("보라")
f.write("\n")
f.write("분홍")
f.write("다빈")
f.close()

with open("text.txt","w", encoding="UTF-8") as f:
    f.write("다빈")
    f.write("보라")
    f.write("\n")
    f.write("분홍")
    f.write("다빈")
#with를 벗어나면 자동으로 닫아줌