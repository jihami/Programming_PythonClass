from baseball_game_engine import make_answer, check
from coustom_error import InvalidLengthError

def save_history(answer, count, name):
    with open('baseball_history.txt', 'a', encoding='utf-8') as f: # a -> append텍스트 계속 써내려감
        f.write(f"{answer}:{count}:{name}\n")

def load_hisorty():
    count_name = {}
    with open("baseball_history.txt", "r", encoding="utf-8") as f:
        print("-"*10, "history", "-"*10)
        while True:
            line = f.readline() #한줄 읽기
            if line == "":  #파일이 끝이며 끝냐기
                break
            print(line.rstrip())    #\n삭제
            line = line.rstrip()    #answer:count:name
            data = line.split(":")  #data[0]: answer, data[1]: count, data[2]: name   :으로 자르기
            count_name[data[1]] = data[2]   #{3: "name"} 하나씩 딕셔너리 만듦
        #top3
        count_name = sorted(count_name.items()) #shift + tab 한칸 앞으로 딕셔너리 정리   정렬하기
        return count_name[:3] #top3가지 보여주기

answer = make_answer()
print(answer)
# 반복


count = 0


while True:
    # 질문
    guess = input('예상 숫자 : (t:history, top3)')
    #t를 입력하면 top3 불러오기
    if guess == "t":
        top3 = load_hisorty()
        print(top3)
        continue #계속 실행
    # 숫자인지 아닌지 확인
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer):
        # raise InvalidLengthError('정답의 길이와 다름니다. 3자리 수를 입력해주세요')
        print(f"정답의 길이와 다른 것 입력{len(answer)}문자")
        continue


    # 결과 판정
    strike, ball = check(guess, answer)
    count += 1
    # 출력
    print(f'{guess}\tstrike: {strike}, ball: {ball}\t{count}try')
    # 정답 == 숫자, 반복 종료
    if answer == guess:
        print('정답입니다.')
        #정답, 시도횟수 저장
        name = input("이름 : ")
        save_history(answer, count, name)
        #불러오기 to3
        top3 = load_hisorty()
        print(top3)
        break