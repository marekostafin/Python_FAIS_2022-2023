def make_ruler(n):
    miarka = "|"
    for i in range(0, n):
        miarka += "....|"

    miarka += "\n0"
    for j in range(1, n + 1):
        for k in range(0, 5 - len(str(j))):
            miarka += " "
        miarka += str(j)

    print(miarka)

def make_grid(rows, cols):
    horizontal = "+"
    vertical = "|"
    for i in range(0, cols):
        horizontal += "---+"
        vertical += "   |"

    horizontal += "\n"
    vertical += "\n"
    rectangle = horizontal

    for i in range(0, rows):
        rectangle += vertical
        rectangle += horizontal

    print(rectangle)