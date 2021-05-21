class Drink:
    _CUPS = ('레귤러', '점보')
    _ICES = ('0%', '50%', '100%', '150%')
    _SUGARS = ('0%', '50%', '100%', '150%')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0  # 레귤러
        self.ice = 2  # 100%
        self.sugar = 2  # 100%

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):  # 컵 종류 보여주자
            print(f'{index + 1}: {cup}')

        # 컵 선택하자
        cup = input('컵사이즈를 선택하세요 : ')
        if cup == "":
            self.cup = 0
        else:
            cup = int(cup)
            # 컵 self에 넣자
            self.cup = cup - 1
        if self.cup == 1 : #점보
            self.price += 500 #점보면 +500
    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):  # 얼음 종류 보여주기
            print(f"{index + 1} : {ice}")
        ice = input("얼음양 선택 : ")  # 선택
        # if ice == "":
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) - 1
        self.ice = 2 if ice == "" else int(ice) - 1  # self.ice에 설정

    def set_sugar(self):
        for index, suger in enumerate(Drink._SUGARS):  # 당도 종류 보여줌
            print(f"{index + 1} : {suger}")
        suger = input("당도 선택 : ")  # 당도 선택
        self.suger = 2 if suger == "" else int(suger) - 1  # self.suger에 넘
    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()
    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}' + f'\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}' + f'\t당도:{Drink._SUGARS[self.sugar]}'
class Coffe(Drink):
    pass
class Bubbletea(Drink):
    _PEARLS = ("타피오카", "화이트", "알로에펄", "코코")
    def __init__(self,name, price):
        super().__init__(name, price) #부모초기화 호출
        self.pearl = 0 #타피오카
    def set_pearl(self):
        for index, preal in enumerate(Bubbletea._PEARLS) : #펄 종류 보여줌
            print(f"{index + 1} : {preal}")
        preal = input("펄 선택 : ")#펄 선택
        self.pearl = 0 if preal == "" else int(preal) -1 #self.preal에 넣기
    def order(self):
        super().order()        #부모클래스의 order() 호출
        self.set_pearl()         #set_preal()호출
    def __str__(self):
        result = super().__str__()  # 부모클래스의 __str__()(이름, 가격, 컵사이즈, 얼음량, 당도), 펄
        return result + f'\t펄종류: {Bubbletea._PEARLS[self.pearl]}'
class Oder:
    def __init__(self):
        self.menu = [] #self.menu 메장에 있는 음료수 전체
        self.init_menu() #init_menu()
        self.order_menu = []#self.order_menu 내가 고른 메뉴들
    def init_menu(self):
        쟈밍 = Coffe('아아', 2500)
        다빈 = Bubbletea("사하라", 3800)
        민식 = Bubbletea("불루베리 스무디", 3800)
        self.menu.append(쟈밍)
        self.menu.append(다빈)
        self.menu.append(민식)
    def show_munu(self):
        for index, drink in enumerate(self.menu):
            print(f"{index+1} : {drink.name} \t {drink.price}원")
    def sum_price(self):
        sum_value = 0#self.order_menu 에서 하나씩 꺼내서 그  Drink 의 가격 합꼐내고 리턴
        for drink in self.order_menu:
            sum_value += drink.price
        return sum_value

    def order_drink(self):
        while True:     #반복문
            self.show_munu()    #메뉴 보여줌
            drink = input("메뉴 선책 : ")      #메뉴선택
            drink = int(drink)-1
            new_drink = self.menu[drink]
            new_drink.order()     #옵션선택
            self.order_menu.append(new_drink)    #self.oreder_menu에 추가
            is_add = input("더 주문하시겠습니까?(n : 졸료) : ")       #더 주문 할껀지
            if is_add == 'n':
                break
        print(self)    #주문내용 출력
    def __str__(self):
        s = '-' * 20 +" 주문 내역 "+"-"*20+ "\n"        #주문내역 제목 보여주기
        for drink in self.order_menu:      #주문한 음료수들 목록 보여주기
            s += str(drink) + "\n"
        s += f"총금액 : {self.sum_price()}원"        #총 합계 가격 보여주기
        return s

# 쟈밍 = Bubbletea("불루베리 요거트", 3000)

# 쟈밍.order()
# print(쟈밍)
order = Oder()
order.order_drink()