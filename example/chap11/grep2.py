# 텍스트 파일만이 들어 있는 디렉토리에서 실행하여야 함
import os
arr = os.listdir()

# 이 프로그램은 현재 디렉토리 안의 텍스트 파일에서 "Python"을 찾는다.

for f in arr:
    print(f)
    try :
        with open(f, "r", encoding="utf-8") as infile:
            for line in infile:
                e = line.rstrip()		# 오른쪽 줄바꿈 문자를 없앤다. 
                if "Python" in e:
                    print(f, ":", e)
            infile.close()
    except Exception as e:
        pass

input()
