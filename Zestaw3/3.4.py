import sys

x = None
while(True):
    try:
        x = input()
        if x == "stop": break
        print("x = {}   x^3 = {}".format(float(x), pow(float(x),3)))
    except:
        print("Wprowadzone dane nie są numeryczne! Proszę wprowadzić liczbę", file=sys.stderr)
        continue
