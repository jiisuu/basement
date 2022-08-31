def make_pizza(bread):
  return f"{bread}+🥫"

def add_one(tomato):
  return f"{tomato}+🍅"

def add_two(potato):
  return f"{potato}+🥔"

dou = make_pizza("🫓")
tomato_pizza = add_one(dou)
potato_pizza = add_two(dou)
perfect_pizza = add_two(tomato_pizza)

print(dou)
print(tomato_pizza)
print(potato_pizza)
print(perfect_pizza)