f = open("text.txt","w", encoding="UTF-8")
f.write("홍다빈")
f.write("분홍")
f.write("\n")
f.write("유바롬")
f.write("보라")
f.close()

with open("text.txt","w", encoding="UTF-8") as f:
    f.write("홍다빈")
    f.write("분홍")
    f.write("\n")
    f.write("유바롬")
    f.write("보라")
#with를 벗어나면 자동으로 닫아줌