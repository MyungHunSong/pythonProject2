#입력.
# from builtins import input
#
# number = input("정수 입력>")
# number = int(number)
#
# if number > 0:
#     raise NotImplementedError
# else:
#     raise NotImplementedError

# else 조건문 활용
import datetime

number1 = input("정수 입력>")
number1 = int(number1)

#조건문을 사용합니다.
if number1 % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#elif 구문

#현재 날짜/ 시간을 구하고
#쉽게 사용할 수 있게 월을 변수에 저장.
now = datetime.datetime.now()
month = now.month
# month = now.month

#조건문으로 계절을 확인
if 3<= month <= 5:
    print("봄이다.")
elif 6<= month <= 8:
    print("여름 ㅅㅂ.")
elif 9<= month <= 11:
    print("가을...")
else:
    print("겨울이라!")

#변수 선언
score = float(input("학점 입력>"))

#조건문 적용.
if score == 4.5:
    print("신")
elif 4.2 <= score <= 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자.")
elif 2.8 <= score < 3.5:
    print("일반인")
elif 2.3 <= score <2.8:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자")
elif 1.0 <= score < 1.75:
    print("백정")
elif 0.5 <= score < 1.0:
    print("벌레")
else:
    print("머하는 새끼임?")




