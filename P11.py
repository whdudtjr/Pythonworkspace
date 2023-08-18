# 어떤 책에서도 나오는 예제
#1부터 10까지의 합을 구해보자

a = 1
sum = 0

while a <= 10:
    sum = sum + a
    a += 1

print(f"1부터 10까지의 합은 {sum}입니다")

# 1부터 10까지의 짝수의 합
x = 1
sum = 0

while x <= 10:
    if x % 2 == 0:
        sum = sum + x
        x += 1
    else:
        pass

print(f"1부터 10까지의 짝수의 합은 {sum}입니다")
 