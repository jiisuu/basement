# 코딩 실습 4 
def 인사말_만들기(이름):
    인사말 = '안녕하세요?' + 이름 + '님'
    return 인사말
    
def 인사말_바로하기(이름):
    인사말 = '안녕하세요?' + 이름 + '님'
    print(인사말)

인사말 = 인사말_만들기('준이')
print(인사말)

인사말 = 인사말_바로하기('정국')

# 코딩 실습 5 
이름 = input('당신의 이름은?')
나이 = int(input('당신의 나이는?'))

print('당신은 ' + 이름 + '이고' + str(나이) + '살 입니다.')
print('당신은', 이름, '이고', 나이, '살입니다.')
print('당신은 {}이고 {}살 입니다.'.format(이름,나이))