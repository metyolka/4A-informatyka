def binarny(liczba):
   wynik = ""   
   while liczba > 0:  
       wynik = str(liczba % 2) + wynik
       liczba = liczba // 2
   return wynik    

liczba = int(input("Podaj liczbe: "))
print(binarny(liczba))