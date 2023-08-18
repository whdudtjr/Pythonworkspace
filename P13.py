# 반복문에는 continue, break 키워드

a = 10

while True:
    print("안녕하세요")
    a += 1
    if a > 15:
        break

a = 10
while a <= 15:
    print("안녕하세요")
    a += 1

a = 0
sum = 0
while a < 10:
    a += 1

    if a % 2 !=0:
        continue
    
    sum += a
print(sum)
    

