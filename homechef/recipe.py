class Recipe:
    def __init__(self, name):
        self.ingredient = {} # 재료, 재료의 개수(양 -------- 빈 딕셔너리 생성
        self.contents=""#내용
        self.name = name #이름
        self.people = 1 #인분
        self.video = "" #영상 url
    def set_contents(self):
        contents = input("레시피 내용 입력 : ")
        self.contents = "입력 정보 없음" if contents == "" else contents

    def set_people(self):
        people = input("인분 입력 : ")
        self.people = "1" if people == "" else people
    def set_video(self):
        video = input("레시피 영상 주소 입력 : ")
        self.video = "입력 정보 없음" if video == "" else video
    def set_ingredient(self):
        while True:
            ingredient = input("재료 입력(ex:'감자 100')  \n 입력완료 후 enter : ")
            if ingredient == "":
                    break
            ingredient_name, ingredient_gram = ingredient.split() #"감자 200".split() -> "감자", "200" 감자는 네임에 200은 그램에
    #         지함 = "지함이는 귀엽다." -> 지함.split() -> "지함이는", "귀엽다"
            self.ingredient[ingredient_name] = ingredient_gram         #{"감자":"200","오이":"100"}

    def __str__(self):
        return f"레시피 : {self.name} \n양 : {self.people}인분 \n정보 : {self.contents} \n재료 : {self.ingredient} \n영상 : {self.video}"
    def set_recipy(self):
        self.set_people()
        self.set_ingredient()
        self.set_contents()
        self.set_video()
카레 = Recipe("카레")
카레.set_recipy()
print(카레)

