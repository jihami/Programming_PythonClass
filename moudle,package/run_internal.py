#math
import math
print(math.ceil(3.5)) #4 천장:올림
print(math.floor(3.5)) #3 바닥:내림
print(round(3.5)) #import할필요 없음 반올림
print(round(3.4)) #import할필요 없음 반올림
print(math.pow(2, 10)) #1024.0
print(math.sin(math.pi/2)) #1.0
print(math.sin(math.pi)) #1.2246467991473532e-16

#random
print("-"*10)
import random
print(random.random()) #java random : 0.0<=r<1.0
print(random.randrange(1, 10)) #1<= r < 10 정수
print(random.randint(1, 10)) #1<=r<= 정수
list1 = ["굶기","피자","김치찜","닭가슴살"]
print(random.choice(list1)) #list1중 1
print("before",list1)
print(random.shuffle(list1)) #list 섞기
print("after",list1)
print(random.sample(list1,2))#list1에서 랜덤으로 n개

#datetime
print("-"*10)
import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.hour)
birthday = datetime.datetime(2004, 11, 29)
print(birthday)
print(now-birthday)