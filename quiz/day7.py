# 다음 중 set을 만드는 방법이 아닌 것?

# 1)  x = {1, 2, 3, 5, 6, 7}
# 2)  x = {}
# 3)  x = set('python')
# 4)  x = set(range(5))
# 5)  x = set()

# 다음 중 변수 i가 6의 배수인지 확인하는 방법으로 올바른 것은?

# 1)  i / 6 == 0
# 2)  i % 6 == 0
# 3)  i & 6 == 0
# 4)  i | 6 == 0
# 5)  i // 6 == 0

# print(10/2)의 출력 결과는 5이다.

# n = input('이름을 입력하세요.')
# print(n.capitalize())
# print(n.upper())

#25 원의 넓이

n = int(input('반지름을 입력하세요.'))
print(n*n*3.14)

#함수로 표현하면
def solution(n):
	return n * n * 3.14

print(solution(int(input())))