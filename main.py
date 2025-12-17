def rozklad(n):
    liczba = 2
    while n > 1:
        if n % liczba == 0:
            print(liczba)
            n //= liczba
 
        else:
            liczba += 1
wartosc = int(input("Podaj liczbę: "))
rozklad(wartosc)