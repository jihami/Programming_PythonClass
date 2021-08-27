class Icecream:
    def __init__(self, name): #생성자 - 변수 초기화
        self.name = name
        #이름 : name
        #설명 : explanaction
    def set_explanation(self, explanation):
        self.explanation = explanation
    def __str__(self):  #객체를 알아보기 쉽게 문자열로 리턴, 주로 print()에서 호출
        return f"이름 : {self.name}"
아이스홈런볼 = Icecream("아이스 홉런볼")
아이스홈런볼.set_explanation("콜릿 아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넛이 쏙쏙!")
요거트31 = Icecream("요거트31")
요거트31.set_explanation("유산균이 살아 있는 오리지널 요거트 아이스크림")
초콜릿무스 = Icecream("초콜릿무스")
초콜릿무스.set_explanation("초콜릿 칩이 들어있는 진한 초콜릿 아이스크림")
베리베리스트로베리 = Icecream("베리베리스트로베리" )
베리베리스트로베리.set_explanation("새콤상큼 딸기 과육이 듬뿍!")

class Order:
    _CATEGORIES = ("싱글레귤러", "더블레귤러", "파인트")
    _PRICE = (3200, 6200, 8200)
    def __init__(self):
        pass
        #종류 : 콘, 파인트....
        self.set_cateries()
        #메뉴
        self.menu = []
        self.init_menu()
        #주문한 메뉴
        self.order_menu = []
    def __str__(self):
        pass
    def set_cateries(self):
        for index, category in enumerate(Order._CATEGORIES):
            print(index+1, category)
        category_num = input("종류를 골라주세요 : ")
        self.category = int(category_num)
    def init_menu(self):
        self.menu.append(Icecream("초콜릿무스"))
        self.menu.append(Icecream("베리베리스트로베리"))
        self.menu.append(Icecream("31요거트"))
        
    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f"{index+1}. {icecream}")
    def order(self): #아이스크림 보여주기
        self.show_menu()
        for _ in range(self.category):  #종류에 따라 반복, 쓰여지지 않는 변수 (for) -> _
            #   메뉴 선택
            icecram = input("아이스크림 선택 : ")
            icecram = int(icecram)
            #   주문한 메뉴에 추가
            self.order_menu.append(self.menu[icecram-1])
        #종료출력
        print("-"*10+" 주문 내역입니다. "+"-"*10)
        print(Order._CATEGORIES[self.category-1])
        print(str(Order._PRICE[self.category-1])+"원")
        #주문한 메뉴 출력
        for icecram in self.order_menu:
            print(icecram)
order = Order()
order.order()