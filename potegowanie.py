def potega_szybka(podstawa, wykladnik):
    wynik = 1
    while wykladnik > 0:
        if wykladnik % 2 == 1:
            wynik = wynik * podstawa
        podstawa = podstawa * podstawa
        wykladnik = wykladnik // 2
    return wynik


def szukaj_bin(tablica, liczba):
    lewy = 0
    prawy = len(tablica) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if tablica[srodek] == liczba:
            return srodek
        elif tablica[srodek] < liczba:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1

# szybkie potęgowanie
a = int(input("Podaj podstawę potęgi: "))
n = int(input("Podaj wykładnik: "))
print("Wynik potęgowania:", potega_szybka(a, n))

# wyszukiwanie binarne
tekst = input("\nPodaj liczby do tablicy :(oddzielone spacją): ")
tablica = list(map(int, tekst.split()))
tablica.sort()  # upewniamy się, że jest posortowana
print("Twoja tablica:", tablica)
x = int(input("Podaj liczbę do wyszukania: "))
pozycja = szukaj_bin(tablica, x)
if pozycja == -1:
    print("Nie znaleziono.")
else:
    print("Znaleziono na pozycji:", pozycja)
 