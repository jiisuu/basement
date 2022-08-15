#6 False ㄱㅏ ㅇㅏ니ㄴ 것은?
# print(bool(None))
# print(bool(1))
# print(bool(""))
# print(bool(0))

#7 변수명으로 사용할 수 없는 것

# age =
# a =
# as = 함수라서 사용못함
# _age =
# 1age = 변수의 이름은 숫자로 시작할 수 없다.

#8 출력값 == 84
# d = {'height':180,'weight':78,'weight':84,'temparture':36,'eyesight':1}
# print(d['weight'])

#9 2019/04/26 11:34:27 이 출력되게 하시오.
# year = '2019'
# month = '04'
# day = '26'
# hour = '11'
# minute = '34'
# second = '27'

# print(year, month, day, sep='/', end=' ')
# print(hour, minute, second, sep=':')

#10 별찍기, 입력 5, 출력 크리스마스 트리
x = int(input('크리스마스트리'))

for i in range(1, x+1):
    for j in range(x+1 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
