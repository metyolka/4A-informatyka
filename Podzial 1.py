def f(x, wsp, st):
    wynik = 0
    i = 0

    while i <= st:
        wynik = wynik + wsp[i] * (x ** (st - i))
        i = i + 1

    return wynik


def podzial(a, b, wsp, st):

    eps = 0.00001  # stała dokładność

    while (b - a) > eps:
        s = (a + b) / 2

        if f(a, wsp, st) * f(s, wsp, st) < 0:
            b = s
        else:
            a = s

    return (a + b) / 2


# --- dane ---
st = int(input("Podaj stopień wielomianu: "))

wsp = []
i = 0

print("Podaj współczynniki od najwyższej potęgi:")

while i <= st:
    wsp = wsp + [float(input("Podaj współczynnik: "))]
    i = i + 1


a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

wynik = podzial(a, b, wsp, st)

print("Miejsce zerowe:", round(wynik, 5))