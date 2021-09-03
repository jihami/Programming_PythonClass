import math
import random
import datetime


#2
def score(num):
    score=(math.trunc(num/10)*10)
    print(score)
score(56)

#3
def rotto():
    numList = []
    for i in range(6):
        num = random.randrange(1, 45)
        numList.append(num)
    print(numList)
rotto()

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

#5
def birthday():
    birthday = datetime.date(2004,8, 25)
    today = datetime.date.today()
    birthtotoday=today-birthday
    print(birthtotoday)
birthday()

#6
def chri():
    chr = datetime.date(2021,12,25)
    today = datetime.date.today()
    day = chr-today
    print(day)
chri()