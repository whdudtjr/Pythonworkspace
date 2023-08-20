# 863은 소수인가?
# (소수는 1과 자신이외의 정수로 나누어지지 않는 수)
# 해당 수가 소수인지를 판별하는 가장 간단한 방법은 X가 주어졌을 때 X를 2부터 X - 1까지의 모든 수로 나누어 보는 것입니다. 
# 만약 2부터 X-1까지의 모든 자연수로 나누었을 때 나누어떨어지는 수가 하나라도 존재하면 X는 소수가 아닙니다

x = 2
x_prime = True                  # True는 '참'이라는 의미이며 초기값을 참으로 정의
for i in range(2,x):            # 2부터 자기자신 -1까지의 수에대해
    if x % i == 0:              # x를 i로 나눈 나머지가 0이면, 
        x_prime = False         # x_prime을 '거짓'의 의미인 False로 바꾸어라

if x_prime == True:
    print ('{}는 소수이다.'.format(x))  # 소수이다를 출력하라
else:
    print ('{}는 소수가 아니다.'.format(x))
    
    
a = 863

while 2 <= a:
    i = 1
    count = 0
    while i <= a:
        if a % i == 0:
            count += 1
        i += 1
    if count == 2:
        print(f"{a}는 소수이다")
        break
    
    
        