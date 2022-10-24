from lineData import line

line = line.replace(",","").replace(".","").replace(";","")
words = line.split()

longestWord = ""
for w in words:
    if len(w) > len(longestWord):
        longestWord = w

print("Najdłuższe słowo :" + longestWord)
print("Długość najdłuszego słowa: " + str(len(longestWord)))