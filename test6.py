# 1+(-2)+3+(-4)+... 과 같은 식으로 계속 더해나갔을 때, 몇까지 더해야 총합이 100이상이 되는지 구하시오.

a = 1
sum = 0

while True:
    if a % 2 != 0:
        sum += a
    else:
        sum -= a
    if sum >= 100:
        print(a)
        break
    a += 1
    
a = 0
sum = 0
i = -1 # 스위칭 변수

while sum < 100:
    i *= -1
    a += 1
    sum += a * i
    
print(a)
