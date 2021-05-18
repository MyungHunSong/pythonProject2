print('하나만 출력1')
print()

# sep 옵션 # end 끝나고 나서 실행
print('하나만 출력2', 'abcd',sep='\n',end="\n\n")
print('결과를 원하는가? 쟁취해라')

print(type('하나만'),type("하나만"),type(12), type(12.5), sep='\n', end='\n\n')

print("동해물과 백두산이 말랏다\n 하느님이 보우하사 우리나라 헬조선\n 무궁화 삼천리 걸으면 다리 터짐 \n")

test_list = ['안녕디지몬','진화안하냐 ㅅㅂ','오']
for i in test_list:
    print(i, end= '\n\n')


print("안녕하세여ㅗ"[0:6])

#슬라이싱 정말 중요하다.
print("안녕하세여ㅗ"[3:], end='\n')
print("안녕하세여ㅗ"[:3], end='\n')

hello="안녕하세요"
print(type(hello), hello[:2], 'hello', sep='\n', end='\n\n')

# res = input('답정너~~~')
# print(" 1입력한 답은 ", res)

a = "10 20 30 40 50".split(" ")
print(type(a), a, sep='\n')

x, y, z = 10, 20, 30
print(x, y, z, sep='\n')
# swap 도랏네 이게 된다고?
print()

x, y = y, x
print(x, y, sep='\n')



