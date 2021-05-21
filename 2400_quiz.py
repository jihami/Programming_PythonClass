
import random
반4 = list(range(1, 20))
반4.remove(3)
print(반4)
print(random.choice(반4))

id_number = "040825"
# print(id_number[0:2])
# print(id_number[:2])
# print(id_number[:-4])
# print(id_number[-6:-4])

# print(id_number[2:])
# print(id_number[2:6])
# print(id_number[-4:])
year = id_number[:2]
print(year)
month_day = id_number[2:]
print(month_day)
# print(int(year)*int(month_day))
print("곱한결과 : ", int(year)*int(month_day))
print("곱한결과 : " + str(int(year)*int(month_day)))

phone_number = "010-2312-7296"
print(phone_number[:phone_number.index("-")])
print(phone_number[-4:])


name = "지함" #따옴표가 없으면 변수명으로 생각
age = 18

# %-formatting
print("안녕 나는 %s 이야. 내 나이는 %d 살이야" %(name,age))
# str.format()
print("안녕 나는 {} 이야. 내 나이는 {} 살이야".format(name, age))
# f-string
print(f"안녕 나는 {name} 이야. 내 나이는 {age} 살이야")

# 내이름 열번 출력
print((name+" ")*10)
# 문자열 + 문자열, 문자열 + 정수형
studen_number = "1404"
# print(studen_number[-2:][1])
print(int(studen_number[-2:]))
