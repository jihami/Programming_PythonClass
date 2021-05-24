from recipe import Recipe

class Recipebook:
    def __init__(self):
        self.recipr_list = []
    def add_recipe(self):
        name = input("레시피 이름 입력 : ")  # 추가할 레시피 입력 입력 받음
        for recipe in self.recipr_list : # 중복 체크 함
            if name == recipe.name : # 중복되는 레시피가 있으면
                print("이미 존재하는 레시피 입니다.")  # 중복된다고 알려줌
                return #함수를 끝낸다는 의미
        new_recipe = Recipe('name')# 없으면 생성
        new_recipe.set_recipy()
        #레시피리스트에 생성한 레시피 추가
        self.recipe_liset.append(new_recipe)

    def __str__(self):
        pass