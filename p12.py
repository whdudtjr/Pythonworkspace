# 어떤 책에서도 나오는 예제
#1부터 100까지의 합을 구해보자

value1 = input("첫번째 값을 입력하세요")
value2 = input("두번째 값을 입력하세요")
value1 = int(value1)
value2 = int(value2)

x = value1
sum = 0

while x <= value2:
    sum = sum + x
    x += 1
   
print(f"{value1}부터 {value2}까지의 합은 {sum}입니다")

a = 1
sum = 0

while a <= 100:
    if a % 2 == 0:
        sum = sum + a
    a += 1
    
print(f"1부터 10까지의 짝수의 합은 {sum}입니다")
