from lineData import line

line = line.replace(",","").replace(".","").replace(";","")
words = line.split()
frontLetters = ""
backLetters = ""
for w in words:
    frontLetters += w[0]
    backLetters += w[-1]

print("Napis z pierwszych liter: " + frontLetters)
print("Napis z ostatnich liter: " + backLetters)