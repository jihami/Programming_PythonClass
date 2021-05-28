from recipe import Recipe

class Recipebook:
    def __init__(self):
        self.recipe_list = []
        self.init_recipe()

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

    def search_ingredient(self):#재료로 해당하는 레시피 찾기
        all_ingredient = set() # 빈 셋(set) 생성 -> 제로를 중복 제거해서 담은 셋(set
        for recipe in self.recipe_list : # 레시피 북에 잇는 레시피 재료를 셋에넣음  한개는 add 두 개씩 쓸때는 update
            for ingredient in recipe.ingredient:
                all_ingredient.add(ingredient)
        for index, ingredient in enumerate(all_ingredient) : # 모든 재료 보여줌
            print(f"{index+1} : {ingredient}")
        search_num = int(input('사용할 재료 입력 : '))#찾을 재료 검색(입력 받음)
        search_ingredient =list (all_ingredient)[search_num-1]
        for recipe in self.recipe_list: #레시피 리스트의 레시피 -> 레시피의 재료를 살펴보자
            if search_ingredient in recipe.ingredient:        # 입력한 재료가 포함되면
                print(recipe)    # 레시피 모두 보여줌
    def init_recipe(self):
        떡볶이 = Recipe("떡볶이")
        떡볶이.people = 2
        떡볶이.video = "알아서 봐라"
        떡볶이.ingredient = {"떡":"200", "고추장":"100", "어묵":"100", "양파":"300","물":"100"}
        self.recipe_list.append(떡볶이)
        카레 = Recipe("카레")
        카레.people = 2
        카레.video = "고에스더 나락"
        카레.ingredient = {"카레가루":"100","감자":"3"}
        self.recipe_list.append(카레)
        파스타 = Recipe("파스타")
        파스타.video = "나도 파스타 무글랭"
        파스타.ingredient = {"면":"200","소스":"400"}
        self.recipe_list.append(파스타)
    def __str__(self):
        pass //안써도 ㄱㅊ
