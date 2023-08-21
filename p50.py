# 설계 문법 - 함수, 클래스

# 함수 선언
# def gugudan():
#     print("안녕")

# gugudan() # 선언된 함수를 호출한다
# print("d")

# def gugudan(a,b):
#     while a <= 9:
#         b = 1
#         while b <= 9:
#             print(f"{a} x {b} = {a*b}")
#             b += 1
#         a += 1
#         break
        
# gugudan(4,1)

def gugudan(start, end):
    x = start
    while x <= end:
        y = 1
        while y <= 9:
            print(f"{x} x {y} = {x * y}")
            y += 1
        x += 1
gugudan(1,4)