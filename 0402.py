#휴대촌 번호를 입력할 때 - 있든, 없든, 없이 출력
phone_number1 = '010-2540-5357'
phone_number2 = '010 7584 1367'
phone_number3 = '01075841367'
phone_number = phone_number1
# 컨트롤 + f => 검색
# result = phone_number1.replace("-", "")
# print(result)
result = phone_number.replace("-", "").replace(" ", "")
print(result)

student_number="2404"
num=int(student_number[1])
majors = ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"]
if 1 <= num <= 6:
    print(f"{num}반 {majors[(num-1)//2]}")  # //->나머지 X , / -> 소수점도 나옴
else:
    print("잘못 입력했습니다.")

# def average(*numbers):
#     count = 0
#     sum_valuse = 0
#     for i in numbers:
#         sum_valuse += i
#         count += 1;
#     return sum_valuse/count
# print(average(10,20,30))
def get_major(student_number):
    majors = ["뉴미디어소프트웨어과","뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어웹솔루션과", "뉴미디어디자인과", "뉴미디어디자인과"]
    grade = student_number[0]
    classroom = int(student_number[1])
    return grade, majors[classroom - 1]

grade, majors = get_major("2404")
print(majors, grade)
#빨간줄에 알트 엔터 치면 오류 고쳐줌

def average(*numbers):
    return sum(numbers)/len(numbers)
print(average(10,20,30))
print(average(4, 23))

def get_bmi(height, weight):
    height /= 100
    bmi = weight/height ** 2
    return round(bmi, 1)


bmi = get_bmi(176, 69)
print(bmi)

if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("정상")
elif bmi < 25:
    print("과체중")
else:
    print("비만")
