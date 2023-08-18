# for 문을 이용해서 
# 1부터 1000까지의 합을 구하는 코드를 작성하되
# 3의 배수만 더하는 코드를 작성하자

sum = 0

for i in range(1,1001):
    if i % 3 == 0:
        sum += i

print(sum)
