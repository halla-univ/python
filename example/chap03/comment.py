# 사용자로부터 화씨온도를 입력받는다.
ftemp = int(input("화씨온도: "))

ctemp = (ftemp-32.0)*5.0/9.0    # 화씨온도->섭씨온도
print("섭씨온도:", ctemp)        # 썹씨온도를 화면에 출력한다.
