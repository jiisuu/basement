#34 sort 확인하기
#입력 : 176 156 155 165 166 169
#출력 : NO

user_input = input()
l = list(user_input.strip().split())
l = [int(i) for i in l]

if l != sorted(l):
    print("NO")

else:
    print("YES")