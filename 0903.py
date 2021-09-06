import math
import random
import datetime

#1
def pay(mon):
    pay = math.trunc(mon/100) *100 #버림 함수
    print(pay)
pay(59827)

#정훈쌤
bill = 59827
print(bill//100*100)
print(bill-bill%100)
print(math.floor(bill/100)*100)
print(int(bill/100)*100)


#2
def score(num):
    score=(math.trunc(num/10)*10)
    print(score)
score(56)

#정훈쌤
score = 93
score = 56
print(round(score/10)*10)
print(round(score, -1))


#3
def rotto():
    numList = []
    for i in range(6):
        num = random.randrange(1, 45)
        numList.append(num)
    print(numList)
rotto()

#정훈쌤
print(random.sample(range(1, 45 + 1), 6))

#4
def ran():
    numList = set()
    while(True):
        if(len(numList)!=3):
            num = random.randrange(1, 9)
            numList.add(num)
        else:
            break
    print(numList)
ran()

#정훈쌤
list_r = random.sample(range(1, 9 + 1), 3)
print(list_r)
# print(str(list_r)) -> 리스트 그대로 출력
print("".join(str(n) for n in list_r)) #for문을 사요앻서 하나씩 뽑아와서 조인함
# join -> 문자열로 합칠때 사용
print("".join(map(str, list_r))) #위에랑 같은 뜻


#5
def birthday():
    birthday = datetime.date(2004,8, 25)
    today = datetime.date.today()
    birthtotoday=today-birthday
    print(birthtotoday)
birthday()

birthd = datetime.datetime(2004,8,25)
now = datetime.datetime.now()
print(now - birthd)

#6
def chri():
    chr = datetime.date(2021,12,25)
    today = datetime.date.today()
    day = chr-today
    print(day)
chri()

christmas = datetime.datetime(2021,12,25)
print(christmas - now)

#7
my_bd = datetime.datetime(2021,8,25)
if my_bd < now :
    my_bd = my_bd.replace(year=2022)
    # my_bd.year += my_bd..year+1  -> 에러 is not writable 맘대로 값 못바꾼대
print(my_bd-now)

#8 랜덤하게 번호로 자리 배치 하기 (전학, 자퇴)

# 마지막 번호 입력 받기
last_number = input("마지막 번호 : ")
# 1~마지막 번호 리스트 생성
list_class = list(range(1, int(last_number)+1))
# 반복
while True:
    exclude_number = input("제외 할 번호(entet->제외안함) : ")#   뺄 번호 묻기
    if  exclude_number == " ":#   반복하기
        break
    list_class.remove(int(exclude_number))#   빼기
    random.shuffle(list_class)# 섞기
    print("자리\t학생번호")
    for i, number in enumerate(list_class):# 출력하기
        print(f"{i+1}\t{number}")
