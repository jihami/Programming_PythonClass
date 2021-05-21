def print_memu():
    print("1. 레시피 검색")
    print("2. 레시피 추가")
    print("3. 재료 검색하기")
    print("4. 전체레시피 보여주기")
    print("5. 종료하기")
    num = int(input("메뉴를 선택하세요 : "))
    return num
def main():
    while True :
        num = print_memu()
        if num == 1 :
            # 레시피 검색
            return
        elif num == 2 :
            #레시피 추가
            return
        elif num == 3 :
            #재료 검색
            return
        elif num == 4 :
            #전체레시피 보여주기
            return
        elif num == 5 :
            #종료하기
            break
        else:
            print("잘못 입력하였습니다. \n 다시 입력하세요")