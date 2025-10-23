def wyszukiwanie_binarne(lista, cel):
    lewy = 0
    prawy = len(lista) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == cel:
            return srodek
        elif lista[srodek] < cel:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1
    
wejscie = input("Podaj posortowaną listę liczb oddzielonych spacją: ")
lista_liczb = list(map(int, wejscie.split()))
cel = int(input("Jakiej liczby szukasz? "))
wynik = wyszukiwanie_binarne(lista_liczb, cel)
if wynik != -1:
    print(f"Znaleziono liczbę {cel} na indeksie {wynik}.")
else:
    print(f"Nie znaleziono liczby {cel} w liście.")
 