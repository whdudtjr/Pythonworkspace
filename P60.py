# 클래스 (설계)
# 객체지향프로그래밍(OOP)

# 속성 + 기능(메소드)

#클래스 선언
class Car:
    def __init__(self, name, fuel, speed, distance):
        # 생성자 - 속성 정의
        self.name = name
        self.fuel = fuel
        self.speed = speed
        self.distance = distance
    # 메소드(기능) : 클래스 안에 선언된 함수, self가 핵심
    def showStatus(self):
        print(f"{self.name}] 연료: {self.fuel}, 현재 거리: {self.distance}")

    def run(self, count):
        x = 0
        while x < count:
            if self.fuel <= 0:
                print(f"{self.name}는 연료 부족")
                break

            self.fuel -= 1
            self.distance += self.speed
            x += 1
  
    
# 인스턴스 생성
c1 = Car("1번 자동차" , 20, 5, 0)
c2 = Car("2번 자동차" , 30, 15, 0)

# 메소드 호출
c1.showStatus()
c2.showStatus()

c1.run(10)
c2.run(50)

c1.showStatus()
c2.showStatus()
# fuel1 = 30
# fuel2 = 20

# speed1 = 5 #연료 1을 쓸 때마다 5만큼 감
# speed2 = 10

# distance1 = 0
# distance2 = 0
# x = 0
# while x < 10:
#     fuel1 = fuel1 - 1
#     distance1 = distance1 + speed1
#     x += 1
# print(f"1번 자동차는 {fuel1}남았고 {distance1}만큼 이동했습니다.")








