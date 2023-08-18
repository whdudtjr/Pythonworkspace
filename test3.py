# 구구단을 출력해보자

# a = 2

# while a <= 9:

#     b = 1
#     while b <= 9:
#         result = a * b
#         print(f"{a} X {b} = {result}") 
#         b += 1
#     a += 1


for i in range(2,10):
    j = 1
    for j in range(1,10):
        result = i * j
        print(f"{i} X {j} = {result}")
        j += 1
    i += 1