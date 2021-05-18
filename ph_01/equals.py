# 값비교
print(10 == 100)
print(10 is 100)
print(10 != 100)
print(10 is not 100)

print()
x = 23;
print("x = ", 20 < x < 30)


print()
if True:
    print("True 입니다.")
    print("정말 true")

if False:
    print("False")

print("aaa")

#입력을 받습니다.
number = input("정수 입력>")
number = int(number)

#양수 조건
if number>0:
    print("양수 입니다.")

#음수 조건
if number<0:
    print("음수 입니다.")

#0 조건
if number==0:
    print("0 입니다.")
print()
# 예시 - 날짜/시간 출력하기.
import datetime

#현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

#출력합니다.
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

# 현재 날짜/ 시간을 구함.
now1 = datetime.datetime.now()

#오전 구분
if now1.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
    
#오후 구분
if now1.hour >= 12:
    print("현재 시각은{}시로 오후입니다.".format(now.hour))

if 3<= now1.month <= 5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))

#끝자리로 짜수와 홀수 구분
number = input("정수 입력>")

#마지막 자리 숫자를 추출
last_char = number[-1]

#숫자로 변환하기
last_number = int(last_char)
#짝수확인
if last_number == 0\
    or last_number == 2\
    or last_number == 4\
    or last_number == 6\
    or last_number == 8:
    print("짝수입니다.")
else :
    print("홀수입니다.")


