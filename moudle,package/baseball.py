from baseball_game_engine import make_answer, check
from coustom_error import InvalidLengthError
answer = make_answer()

# 반복
while True:
    # 질문
    guess = input('예상 숫자 : ')
    # 숫자인지 아닌지 확인
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer):
        raise InvalidLengthError('정답의 길이와 다름니다. 3자리 수를 입력해주세요')

    # 결과 판정
    strike, ball = check(guess, answer)
    # 출력
    print(f'{guess}\tstrike: {strike}, ball: {ball}')
    # 정답 == 숫자, 반복 종료
    if answer == guess:
        print('정답입니다.')
        break