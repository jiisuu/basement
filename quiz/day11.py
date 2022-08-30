#33 로꾸꺼

# n = input()
# r = list(reversed(n))
# print(r)

n = input()
l = list(n.strip().split()) #n의 앞 뒤 공백 없애고, 스페이스바 기준으로 나눠서 리스트 만들기
len1 = len(l) - 1 #인덱스에 넣어야 하니까 -1
for i in range(len1, -1, -1): #거꾸로, 하나씩
	print(l[i], end=' ') #1 2 3 4 5 일때, ㅣ[4] ㅣ[3] ㅣ[2] ㅣ[1] ㅣ[0]

