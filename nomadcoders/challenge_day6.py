numbers = [
    1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️",
    10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16
]

add_num = 0

for number in numbers:
    if type(number) == int:
      add_num += number

print(add_num)