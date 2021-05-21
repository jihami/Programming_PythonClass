'''# 2단부터 7단 출력
for dan in range(2, 9+1): #2~9
    for i in range(1, 9 + 1): #x1~x9
        print(f"{dan} x {i} = {dan * i}")
    print()
    if dan == 7:
        break
'''
# 2단부터 7단 출력하되, x1,x3,x5,x7 x9 인것만 출력
for dan in range(2, 9 + 1): #2~9
    for i in range(1, 9 + 1): #x1~x9
        # if i == 2 or i == 6 or i == 8 :
        if i % 2 == 0:
            continue
        print(f"{dan} x {i} = {dan * i}")
    print()
    if dan == 7:
        break

