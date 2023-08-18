# 구구단을 출력을 하되 7단과 6단을 제외하고 출력하자.

# a = 2
# while a <= 9:
#     b = 1
#     while b <= 9:
#         if a == 6 or a == 7:
#             break
#         result = a * b
#         print(f"{a} X {b} = {result}")    
#         b += 1
#     a += 1

a = 2
while a <= 9:
    b = 1
    if not (a == 6 or a == 7):
        while b <= 9:
            result = a * b
            print(f"{a} X {b} = {result}")    
            b += 1
    a += 1

a = 2

while a<=9:
    if a == 6 or a == 7:
        a += 1
        continue
    b = 1
    while b <= 9:
        result = a * b
        print(f"{a} X {b} = {result}")
        b += 1 

    a += 1    