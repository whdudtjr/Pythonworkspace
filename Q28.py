# 1~10000사이에 8이 몇번 나오는가?

start = 1
end = 10000

count = 0

value = start

while value <= end:
    temp = value
    while True:
        if temp%10 == 8:
            count += 1
        temp = temp//10
        if temp == 0:
            break
    value += 1
    
print(count)