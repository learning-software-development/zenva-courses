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

# 5. Tupels and Ranges

profile = ("Barry", 27)
name = profile[0]
print(type(profile))

my_range = range(5)
print(type(my_range))

# 6. Dictionaries

inventory = {"Axe": 1, "Fruit": 5, "Knife": 1}
print(type(inventory))
print(inventory.items())
num_axes = inventory["Axe"]
print(num_axes)


# 7. If Statements

pos = 5
key = "R"

if key == "R":
    pos += 10
    print("Player moved right")
elif key == "L":
    pos -= 10
    print("Player moved left")
else:
    print("Unknown command")

# 8. While Loops

key = "Q"

while isGameOver:
    print("The game is running...")
    if key == "Q":
        isGameOver = False

print("The game is over.")

# 9. For Loops

for count in range(4):
    print(count + 1)

inventory = ["Axe", "Shield", "Boots"]

for item in inventory:
    print(item)

# 10. Functions

def move(amount):
    global pos
    pos += amount

move(5)
print("Position", pos)

def move_from(pos, amount):
    return pos + amount

print(move_from(0, 8))

# 11. Classes and Objects

class Hobgoblin():
    def __init__(self):
        self.name = "Hobgoblin"
        self.health = 0
        self.attack = 2

    def bite(self):
        print("The Hobgoblin bites!")

    def run_away(self):
        print("The Hobgoblin runs away.")

character = Hobgoblin()
print(type(character))
