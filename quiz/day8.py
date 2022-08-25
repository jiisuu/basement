#행성 문제 2 - 행성의 한글 이름을 입력하면 영어 이름을 반환하는 프로그램을 만들어 주세요.
# planets = {
#     "수성":"Mercury",
#     "금성":"Venus",
#     "지구":"Earth",
#     "화성":"Mars",
#     "목성":"Jupiter",
#     "토성": "Saturn",
#     "천왕성":"Uranus",
#     "해왕성":"Neptune"}

# n = input('행성 이름을 입력하세요')
# print(planets.get(n))
# print(planets[n])

#27 딕셔너리 만들기
a = input().split()
b = map(int, input().split())

print(b)
result = dict(zip(a, b))
print(result)