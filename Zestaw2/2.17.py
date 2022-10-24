from lineData import line

line = line.replace(",","").replace(".","").replace(";","")
words = line.split()

print("Alfabetycznie: " + str(sorted(words, key=str.lower)))
print("Po długości: " + str(sorted(words, key=len)))