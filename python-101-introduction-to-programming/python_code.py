# 1. Intro to Python

print("Hello, world!")

text = input("Type some text: ")
print("You typed", text)

# 2. Variables

age = 35
print(type(age))

money = 10.50
print(type(money))

isGameOver = False
print(type(isGameOver))

print(type(text))

# 3. Operators

# Assignment: =
# Arithmetic: + - * / % // **
# Comparison: == != >= > <= <
# Logical: and or not

# 4. Lists

inventory = ["Axe", "Food", "Helmet"]

food = inventory[1]
print(food)
inventory[1] = "Fruit"
print(inventory[0:2])

inventory.append("Water")
inventory.remove("Axe")
inventory.insert(1, "Knife")
print(inventory)
