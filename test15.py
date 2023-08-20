# 2~100사이의 소수를 구해보자

# break , continue 정리
# a = 0
# b = 0
# sum = 0
# while a < 5:
#         sum += a
#         a += 1
#         print(sum)
#         while b < 6:
#             sum += b
#             b += 2
#             print(sum)
#             continue     # 제일 가까운 while문으로 돌아가서 실행을 다 한 후, 그 위에 있는 while문 마저 실행
#             break        # break: 제일 위에 있는 while문으로 돌아가서 다시 순차적 진행
            
        

# 

# 소수, 즉 1과 자기 자신만 가지고 있어야 한다, 즉 약수가 2개이면 소수인것이다

a = 2
while a <= 100:
    count = 0
    i = 1
    while i <= a:
        if a % i == 0:
            count += 1
        i += 1
    if count == 2:
        print(a)
        
    a += 1
    
    








