class Recipe:
    def __init__(self, name):
        self.ingredient = [] #재료, 재료의 개수(양
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

    def __str__(self):
        pass