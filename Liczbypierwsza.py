def liczby_pierwsze_do(n):
    for liczba in range(2, n + 1):
        pierwsza = True
        for i in range(2, liczba):
            if liczba % i == 0:
                pierwsza = False
                break
        if pierwsza:
            print(liczba)

n = int(input("Podaj górną granicę zakresu: "))
liczby_pierwsze_do(n)