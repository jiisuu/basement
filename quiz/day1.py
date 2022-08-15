#1
# from readline import insert_text


# nums = [100,200,300,400,500]
# nums.remove(400)
# nums.remove(500)
# print(nums)

#2
# l = [200,100,300]
# l.insert(2,1000)

# print(l)

#3
# l = [100, 200, 300]
# print(type(l))

#4
# 다음 변수 a를 print(type(a))로 넣었을 때 출력될 값과의 연결이 알맞지 않은 것은? 3

# 1)  입력 : a =1,   출력 : class 'int'
# 2)  입력 : a = 2.22,   출력 : class 'float'
# 3)  입력 : a = 'p',   출력 : class 'char' ---> 'str'
# 4)  입력 : a = [1, 2, 3],   출력 : class 'list'

#5 출력값으로 알맞은 것은?
a = 10
b = 2
for i in range(1, 5, 2): #1에서 4까지 2씩, 1,3
    a += i
    
print(a+b)
