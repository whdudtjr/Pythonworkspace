#1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+3+...+10)의 결과를 계산하시오.

# 첫번째 방법 - 문제풀이 그대로, 별찍기 문제
x = 1
sum = 0
while x <= 10:

    y=1
    while y <= x:
        sum = sum + y
        y += 1
    x += 1
print(sum)

# 두번째 방법 - 변수의 적절한 활용방법
x = 1
tempSum = 0
sum = 0
while x <= 10:
    tempSum += x
    sum += tempSum
    x += 1

print(sum)

# 세번째 방법 - 문제의 재구성(아이디어 측면, 정답으로써는 의미 X)

x = 1
sum = 0

while x <= 10:
    sum += x * (11-x)
    x += 1

print(sum)
