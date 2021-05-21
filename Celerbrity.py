class Celerbrity:
    def __init__(self, name): #생성자 메서드
        #이름
        self.name = name
        #group
    def set_name(self, name):
        self.name = name
    def set_entertainment(self, entertainment):
        self.entertainment = entertainment
    def __str__(self): #스트링화 할때 자동으로 생성
        return f"이름 : {self.name}\t소속사 : {self.entertainment}"

class Talent(Celerbrity):
    def __init__(self, name):
        super().__init__(name) #Celerbrity  클래스의 생성자 호출
    def set_drama(self, drama):
        self.drama = drama
    def __str__(self):
        return super().__str__()+f"\t드라마 : {self.drama} "
        # return f"이름 : {self.name} \t 소속사 : {self.entertainment}"
class Singer(Celerbrity):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song
    def __str__(self):
        return super().__str__()+f"\t 노래 : {self.song}"
현진 = Singer("현진", "신메뉴")
현진.set_entertainment("JYP")
print(현진)

필릭스 = Singer("필릭스", "Back Door")
필릭스.set_entertainment("JYP")
print(필릭스)

스트레이키즈 = []
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)
print(스트레이키즈)

# for i in 스트레이키즈: #i:현진 객체, 필릭스 객체
#     print(i)
for i in range(len(스트레이키즈)): #i:0,1
    print(스트레이키즈[i])
IU = Celerbrity("아이유") #new Celerbrity() -> java
# IU.set_name("이지은")
IU.set_entertainment("이담")
#print(IU.name, IU.entertainment)
print(IU) #클래스의 __str__()호출

수지 = Celerbrity("수지")
수지.set_name("배수지")
수지.set_entertainment("JYP")
print(수지)

이광수 = Talent("이광수")
이광수.set_entertainment("킹콩")
이광수.set_drama("라이브")
print(이광수)


