def calculate_area (radius):
    global area 			# 전역변수 area를 사용하겟다고 알림
    area = 3.14 * radius**2
    return

area = 0
r = float(input("원의 반지름: "))
calculate_area(r)
print(area)
input()