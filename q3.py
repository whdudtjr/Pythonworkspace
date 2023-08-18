# 1+(-2)+3+(-4)+... 과 같은 식으로 계속 더해나갔을 때, 몇까지 더해야 총합이 100이상이 되는지 구하시오.

# 문제풀이 1번
x = 1
sum = 0

while True:

    if x % 2 != 0:
        sum = sum + x
    else:
        sum = sum - x
    
    
    if sum >= 100:
        print(x)
        break

    x += 1


# 문제풀이 2번

x = 0
sum = 0
i = -1 #스위칭 변수
while sum < 100:
    i *= -1
    x += 1
    sum = sum + (x*i)

    
print(x)




