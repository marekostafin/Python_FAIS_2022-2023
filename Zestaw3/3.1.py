# Ten fragment jest OK - średniki są w Pythonie dozwolone, jednak nie są wymagane
# Pozwalają one oddzielać wiele poleceń w tej samej linii (jak w tym przykładzie)
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# Poniższa linia jest nieprawidłowa - nielegalne jest wypisywanie więcej niż jednego bloku instrukcji po dwukropku
for i in "axby": if ord(i) < 100: print (i)

# Tu jednak jest OK
for i in "axby": print (ord(i) if ord(i) < 100 else i)
