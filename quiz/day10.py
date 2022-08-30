
#32 문자열을 입력받으면 단어의 갯수를 출력하는 프로그램
sentence = input()
l1 = sentence.split().strip()
print(len(l1))
print(type(l1))

sentence = input()
l2 = sentence.strip().split()
print(len(l2)) 
print(type(l2))

# n = input()
# l = list(n.strip().split())
# print(len(l)) ##test1 test2 tes3 ₩

test = "test".split("s")
print(test)

test2 = "test test2".strip()
test3 = "   test   test2   ".strip()

print(test2)
print(test3)