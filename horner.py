def horner(wsp, st, x):
    if st == 0:
        return wsp[0]
    return x * horner(wsp, st - 1, x) + wsp[st]
# K2, K3
stopien = int(input("Podaj stopien wielomianu: "))
# K4
wsp = [0] * (stopien + 1)
# K5, K6
i = stopien
while i >= 0:
    wsp[i] = int(input(f"Podaj wspolczynnik stojacy przy potedze {i}: "))
    i -= 1
# K7
x = float(input("Podaj argument: "))
# K8
wynik = horner(wsp, stopien, x)
# wynik
print(f"W( {x} ) = {wynik}")