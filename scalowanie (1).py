def scalaj(tab):
    if len(tab) > 1:
        srodek = len(tab) // 2
        lewa = tab[:srodek]
        prawa = tab[srodek:]
        scalaj(lewa)
        scalaj(prawa)
        i = 0
        j = 0
        k = 0
        while i < len(lewa) and j < len(prawa):
            if lewa[i] < prawa[j]:
                tab[k] = lewa[i]
                i += 1
            else:
                tab[k] = prawa[j]
                j += 1
            k += 1
        while i < len(lewa):
            tab[k] = lewa[i]
            i += 1
            k += 1
        while j < len(prawa):
            tab[k] = prawa[j]
            j += 1
            k += 1

tablica = []
ile = int(input("Ile liczb chcesz podac? "))
for i in range(ile):
    liczba = int(input("Podaj liczbe: "))
    tablica.append(liczba)
print("Przed sortowaniem:")
print(tablica)
scalaj(tablica)
print("Po sortowaniu:")
print(tablica)
 