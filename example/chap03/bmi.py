weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))
bmi = (weight / (height**2)) # 지수 연산자를 사용해보자.
print("당신의 BMI=", bmi)
