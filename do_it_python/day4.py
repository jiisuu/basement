# # 코딩 실습 9 
# 전체식권수 = int(input('식권이 몇 장 필요한가요?'))

# for 출력식권 in range(1, 전체식권수 + 1):
#     print('[식권] 번호:', 출력식권)

# # 코딩 실습 10
# 시작단 = int(input('구구단 시작 단을 입력하세요(1~9):'))
# 끝단 = int(input('구구단 끝 단을 입력하세요(1~9):'))

# 출력값 = ''

# for 앞수 in range(시작단, 끝단+1):
#     for 뒷수 in range(1, 10):
#         지금값 = '{}x{}={}\n'.format(앞수, 뒷수, 앞수*뒷수)
#         출력값 = 출력값 + 지금값
        
# print(출력값)

#코딩 실습 11
줄스타일 = input('각 단을 구분하는 줄 모양을 입력하세요:')
출력값 = ''

for 앞수 in range(2,10):
    for 뒷수 in range(1,10):
        지금값 = '{}x{}={}\n'.format(앞수, 뒷수, 앞수 * 뒷수)
        출력값 += 지금값 + '\n'

    if 앞수 == 9:
        pass
    else:
        출력값 += 줄스타일 + '\n'

print(출력값)

