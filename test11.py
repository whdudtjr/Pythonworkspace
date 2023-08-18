# 1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+3+...+10)의 결과를 계산하시오.

a = 1
sum = 0
tempSum = 0
while a <= 10:
    sum += a # 1+2+3 
    tempSum += sum # 1 + 3 + 6
    a += 1
print(tempSum)

a = 1
sum = 0

while a <= 10:
    b = 1
    while b <= a:
        sum += b
        b += 1
    a += 1

print(sum)