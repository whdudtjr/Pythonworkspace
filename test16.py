# 방정식 2x+4y=10의 모든 해를 구하시오. 
# 단, x와 y는 정수이고 각각의 범위는 0<=x<=10, 0<=y<=10 이다.
# 실행 결과)
# x=1, y=2
# x=3, y=1
# x=5, y=0

# 변수 x,y가 있고 x가 이거 일 때 y가 그거고 만약 그 둘을 식에 대입해서 합이 10이면 x 값, y 값 출력

x = 0

while x <= 10:
    y = 0
    while y <= 10:
        if (2 * x) + (4 * y) == 10:
            print(f"x = {x}, y = {y}")
        y += 1
    x += 1