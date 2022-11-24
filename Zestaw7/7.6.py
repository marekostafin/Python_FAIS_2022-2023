# (a) zwracający 0, 1, 0, 1, 0, 1, ...

class switch_iter:
    "Iterator zwracający na przemian 0 i 1"

    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num = (num + 1) % 2
        return num

# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D]

import random

class random_compass_iter:
    "Iterator losowo zwracający \"N\", \"E\", \"S\" lub \"W\""

    def __init__(self):
        self.curr = random.choice(["N", "E", "S", "W"])

    def __iter__(self):
        return self

    def __next__(self):
        curr = self.curr
        self.curr = random.choice(["N", "E", "S", "W"])
        return curr


# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia]

class weekday_numbers_iter:
    "Iterator zwracający kolejno numery od 0 do 6"

    def __init__(self):
        self.day = 0

    def __iter__(self):
        return self

    def __next__(self):
        day = self.day
        self.day = (day + 1) % 7
        return day