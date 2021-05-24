from recipe import Recipe

class Recipebook:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self):
        name = input("레시피 이름 입력 : ")  # 추가할 레시피 입력 입력 받음
        for recipe in self.recipe_list : # 중복 체크 함
            if name == recipe.name : # 중복되는 레시피가 있으면
                print("이미 존재하는 레시피 입니다.")  # 중복된다고 알려줌
                return #함수를 끝낸다는 의미
        new_recipe = Recipe(name)# 없으면 생성
        new_recipe.set_recipy()
        #레시피리스트에 생성한 레시피 추가
        self.recipe_list.append(new_recipe)

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list) :
            print(f"{index+1}")
            print(recipe)

    def search_recipe(self):
        searched_recipe = [] #찾아진 레시피를 저장
        name = input("원하는 레시피 검색 : ")#찾을 레시피이름 입력 받음
        for recipe in self.recipe_list: #찾는게 있는지 리스토돌면서 찾기
            if name == recipe.name: #있으면
                print(recipe) #출력
                searched_recipe.append(recipe)
        if len(searched_recipe) == 0: #검색된 레시피가 없다면 (searched_recipe가 비어있다면)
            answer = int(input("찾는레시피 없음 추가 하시겠습니까?'(ex:1예, 0:아니오)' : "))# 추가할지 물어봄
            if answer : #ㅊ참은 1이기 때문에 실행 ㄱㄴ#추가한다하면
                self.add_recipe()#추가함
            else:
                return


    def __str__(self):
        pass