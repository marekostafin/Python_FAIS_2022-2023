L = [1, 22, 333, 5, 412, 53, 42, 9, 51]

text = ""
for l in L:
    text += str.zfill(str(l), 3)
    text += " "

print(text)