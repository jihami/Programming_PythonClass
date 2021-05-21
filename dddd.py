'''Quiz3-1. n_sum() 함수를 만든다.
함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면,
각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''
import math
# 퀴즈 3-1
# def n_sum(argument):
#     num = str(argument)
#     sum = 0
#     if len(num) >= 10:
#         return -1
#     for i in range(len(num)):   #num='331', 3 012
#         sum += int(num[i])
#     return sum


#
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1
# print("---------------")

# 퀴즈 3-2
def get_subway_fare(km):
    if km < 10:
        pay = 720
        return pay
    elif km < 50 :
        pay = 720
        add = math.ceil((km-10)/5)
        # for i in range(add):
        #     pay += 100
        pay+=(100*add)
        return pay
    elif km > 50 :
        pay = 720 + (50-10)//5 * 100    #1520
        add = math.ceil((km-50)/8)
        # for i in range(add):
        #     pay+= 100
        pay +=(100*add)
        return pay

fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(25)
print(fare)        #1020
fare = get_subway_fare(61)
print(fare)        #1720
print("---------------")

# 퀴즈 3-3
def get_three_six_nine(num):
    s_sum=str(num)
    result = ""
    cont = (s_sum.count('3')+s_sum.count('6')+s_sum.count('9'))
    if cont <= 0:
        result = s_sum
    else:
        for j in range(cont) :
            result += "짝"
    return result

result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝

print("---------------")
# 퀴즈 3-4
'''
chang()를 만든다 함수의 인수(num)를 정수형으로 입력 받아 초로 변환해 리턴하는 함수를 만든다
input함수 이용
'''
def chang(num):
    sec = int(num)* 60 * 60;
    return sec
num = input('시간을 입력하세요: ')
print(chang(num))
