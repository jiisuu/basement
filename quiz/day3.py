#11 1 부터 100 까지 더하기
# s = 0

# for i in range(1, 101):
# 	s += i
# print(s)

#12 
# class Wizard:
#     def __init__(self, health, mana, armor):
#         self.health = health
#         self.mana = mana
#         self.armor = armor

#     def attack(self):
#         print("파이어볼")

# x = Wizard(health = 545, mana = 210, armor = 10)
# print(x.health, x.mana, x.armor)
# x.attack()

#13 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성 몇 번째 행성인지?

planet = ["수성", "금성", "지구", "화성", "목성", "토성", "천왕성", "해왕성"]

n = int(input()) - 1
print(planet[n])
