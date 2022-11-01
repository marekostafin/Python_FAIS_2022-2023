x = input("x = ")
y = input("y = ")

horizontal = "+"
vertical = "|"
for i in range (0, int(x)):
    horizontal += "---+"
    vertical += "   |"

horizontal += "\n"
vertical += "\n"
rectangle = horizontal

for i in range(0, int(y)):
    rectangle += vertical
    rectangle += horizontal

print(rectangle)