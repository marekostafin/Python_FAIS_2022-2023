from lineData import line

line = line.replace(",","").replace(".","").replace(";","")
words = line.split()
lettercount = 0
for w in words:
    lettercount += len(w)

print(lettercount)