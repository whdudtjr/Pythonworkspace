# 구구단의 짝수 단(2, 4, 6, 8단)만 출력하는 프로그램을 작성하되, 
# 2단은 2X2까지, 4단은 4X4까지, 6단은 6X6까지 8단은 8X8까지만 출력하도록 구현하자.

a = 2

while a <= 9:
    if not (a % 2 != 0):
        b = 1
        while b <= a:
            result = a * b
            print(f"{a} X {b} = {result}")
            b += 1
    a += 1
