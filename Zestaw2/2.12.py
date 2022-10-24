line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n" \
       "Aenean non elementum mi.\tNulla lobortis tincidunt mi.\n" \
       "Suspendisse quis velit a."

line = line.replace(",","").replace(".","").replace(";","")
words = line.split()
frontLetters = ""
backLetters = ""
for w in words:
    frontLetters += w[0]
    backLetters += w[-1]

print("Napis z pierwszych liter: " + frontLetters)
print("Napis z ostatnich liter: " + backLetters)