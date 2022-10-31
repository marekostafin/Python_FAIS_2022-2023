L = [3, 5, 4] ; L = L.sort() # OK

x, y = 1, 2, 3 # Próbujemy przypisać trzy wartości do dwóch zmiennych

X = 1, 2, 3 ; X[1] = 4 # Krotki są niezmienne

X = [1, 2, 3] ; X[3] = 4 # Lista nie posiada indeksu "3" - ma indeksy od 0 do 2

X = "abc" ; X.append("d") # Stringi są niezmienne

L = list(map(pow, range(8))) # Funkcja pow potrzebuje dwóch argumentów, a podany został jeden