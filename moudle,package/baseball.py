from baseball_game_engine import make_answer, check

answer = make_answer()

# 반복
while True:
    # 질문
    guess = input('예상 숫자 : ')
    # 숫자인지 확인
    guess_int = int(guess)
    print(guess_int)
    # 결과 판정
    strike, ball = check(guess, answer)
    # 출력
    print(f'{guess}\tstrike: {strike}, ball: {ball}')
    # 정답 == 숫자, 반복 종료
    if answer == guess:
        print('정답입니다.')
        break