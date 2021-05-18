# array 바라
array = [273, 32, 103, "문자열", True, False]
print(array)
#list
list_a = [273, 32, 103, "문자열", True, False]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[3])
print()

print("음수 -1 = ",list_a[-1])
print("음수 -2 = ",list_a[-2])
print("음수 -3 = ",list_a[-3])

print()
list_b = [273, 32, 103]
list_b[0] = "변태"
print("list_b[0] = ",list_b)

# 2차원 배열
list_c = [273, 32, 103, "문자열", True, False]
print(list_c[3])
print(list_c[3][0])
# 아니 파이썬 for 문이다.
list_c = [i for i in list_a]
print(type(list_c), list_c)

#~ 100까지 짝수만 list(even_list)에 저장하고 출력하시오.
#~ 100까지 홀수만 list()에 저장하고 출력하시오.
even_list = [i for i in range(101) if i % 2 ==0]
print(type(even_list),even_list)

odd_list = [i for i in range(101) if i % 2 == 1]
print(type(odd_list),odd_list)

print()
# 2중 루트
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 11]
numberTO100 = [i for i in numbers if i >= 100]
print("for (비교후 맞는수만 빼오기) 100 이상의 수", numberTO100)

print()
list_of_list = [[1,2,3],[4,5,6,7],[8,9]]
for sub_list in list_of_list:
    for i in sub_list:
        print("2중 for문 레스기릿",i)
