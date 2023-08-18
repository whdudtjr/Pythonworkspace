# 1부터 200까지의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.

a = 1
sum = 0

while a <= 200:
    if not (a % 2 == 0 or a % 3 == 0):
        sum += a
    a += 1
print(sum)

