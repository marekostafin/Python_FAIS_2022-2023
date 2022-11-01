length = input()
miarka = "|"
for i in range(0, int(length)):
    miarka += "....|"

miarka += "\n0"
for j in range(1, int(length)+1):
    for k in range(0, 5-len(str(j))):
        miarka += " "
    miarka += str(j)

print(miarka)