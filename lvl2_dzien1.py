# f-strings_01.py

# Załóżmy, że przeprowadziliśmy serię eksperymentów
# i chcemy sformatować ich wyniki w czytelny sposób.

nazwa_eksperymentu = "Test wpływu pH na aktywność enzymu"
pH = 7.4
aktywnosc_enzymu = 0.6752  # Aktywność enzymu jako wartość względna

# Aktywnosc_enzymu zaokrąglona do dwóch miejsc po przecinku i przekonwertowana na procenty:
aktywnosc_enzymu = round(aktywnosc_enzymu * 100, 2)


# Użycie f-stringa do sformatowania opisu
opis_wynikow = "Eksperyment: " + nazwa_eksperymentu + "; " + "przy pH: " + str(pH) + ", " + \
                 "zaobserwowano aktywność enzymu na poziomie: " + str(aktywnosc_enzymu) + "%."

print(opis_wynikow)


# f-strings_02.py

# Załóżmy, że przeprowadziliśmy serię eksperymentów
# i chcemy sformatować ich wyniki w czytelny sposób.

nazwa_eksperymentu = "Test wpływu pH na aktywność enzymu"
pH = 7.4
aktywnosc_enzymu = 0.6752  # Aktywność enzymu jako wartość względna

# Użycie f-stringa do sformatowania opisu
opis_wynikow = (f"Eksperyment: {nazwa_eksperymentu}; "
                f"przy pH: {pH}, "
                f"zaobserwowano aktywność enzymu na poziomie: {aktywnosc_enzymu:.2%}.")

print(opis_wynikow)

# f-strings_03.py

ilosc_probek = 25
srednia = 7.8
odchylenie_standardowe = 0.45

analiza_statystyczna = (f"Przeanalizowano {ilosc_probek} próbek, "
                        f"średnia wartość pH wynosi: {srednia:.1f}, "
                        f"przy odchyleniu standardowym: {odchylenie_standardowe:.2f}.")

print(analiza_statystyczna)

# list-comp_01.py

# Lista wartości pH dla różnych próbek wodnych.
wartosci_pH = [6.5, 7.2, 7.0, 8.3, 6.8, 4.9, 7.3, 6.1, 5.5, 7.8]

# Pusta lista, która będzie zawierała wartości kwaśne pH.
kwasy_pH = []

# Użycie pętli for do iteracji przez listę wartości pH i dodawanie do listy tylko kwaśnych wartości.
for pH in wartosci_pH:
    if pH < 7:
        kwasy_pH.append(pH)

print(f'Wartości kwaśne pH: {kwasy_pH}')

# list-comp_02.py

# Lista wartości pH dla różnych próbek wodnych.
wartosci_pH = [6.5, 7.2, 7.0, 8.3, 6.8, 4.9, 7.3, 6.1, 5.5, 7.8]

# Użycie list comprehension do wyodrębnienia wartości kwaśnych (pH < 7).
kwasy_pH = [pH for pH in wartosci_pH if pH < 7]

print(f'Wartości kwaśne pH: {kwasy_pH}')

# list-comp_03.py

temperatury_celsius = [0, 10, 20, 30, 40]

# Konwersja temperatur z C na F
temperatury_fahrenheit = [(celsius * 9/5) + 32 for celsius in temperatury_celsius]

print(f'Temperatury w Fahrenheitach: {temperatury_fahrenheit}')

# list-comp_04.py

nazwy = ['Drosophila melanogaster', 'Homo sapiens', 'Escherichia coli']
klasy = ['Owad', 'Ssak', 'Bakteria']

# Tworzenie listy słowników reprezentujących organizmy
organizmy = [{'nazwa': nazwa, 'klasa': klasa} for nazwa, klasa in zip(nazwy, klasy)]

print(f'Lista organizmów: {organizmy}')


# list-comp_05.py

sekwencje = ['ATCGGTAG', 'GGGCGC', 'TTATTA', 'CGATATCGAT']

# Obliczanie procentowej zawartości GC dla każdej sekwencji
zawartosc_GC = [(sekwencja.count('G') + sekwencja.count('C')) / len(sekwencja) * 100 for sekwencja in sekwencje]

print(f'Procentowa zawartość GC w sekwencjach: {zawartosc_GC}')


# matplot_01.py

import matplotlib.pyplot as plt

# Dane wejściowe: sekwencje DNA
sekwencje = ['ATCGGTAG', 'GGGCGC', 'TTATTA', 'CGATATCGAT']

# Obliczanie procentowej zawartości GC dla każdej sekwencji
zawartosc_GC = [(sekwencja.count('G') + sekwencja.count('C')) / len(sekwencja) * 100 for sekwencja in sekwencje]

# Wydrukowanie wyników
print(f'Procentowa zawartość GC w sekwencjach: {zawartosc_GC}')

# Tworzenie wykresu słupkowego
plt.bar(range(len(sekwencje)), zawartosc_GC, tick_label=sekwencje)

# Dodawanie tytułu i etykiet
plt.title('Procentowa zawartość GC w sekwencjach DNA')
plt.xlabel('Sekwencje')
plt.ylabel('Procentowa zawartość GC (%)')

# Wyświetlenie wykresu
plt.show()

# funkcje_01.py

lista_liczb1 = [10, 20, 30, 40, 50]
suma1 = sum(lista_liczb1)
liczba_liczb1 = len(lista_liczb1)
print(suma1 / liczba_liczb1)

lista_liczb2 = [11, 20, 33, 40, 50]
suma2 = sum(lista_liczb2)
liczba_liczb2 = len(lista_liczb2)
print(suma2 / liczba_liczb2)

lista_liczb3 = [12, 1110, 15, 430, 540]
suma3 = sum(lista_liczb3)
liczba_liczb3 = len(lista_liczb3)
print(suma3 / liczba_liczb3)

lista_liczb4 = [13, 20, 630, 88, 50]
suma4 = sum(lista_liczb4)
liczba_liczb4 = len(lista_liczb4)
print(suma4 / liczba_liczb4)

lista_liczb5 = [14, 50, 3111, 12, 50]
suma5 = sum(lista_liczb5)
liczba_liczb5 = len(lista_liczb5)
print(suma5 / liczba_liczb5)

# funkcje_02.py

def srednia_liczb(lista_liczb):
    """Funkcja obliczająca średnią arytmetyczną z listy liczb."""
    suma = sum(lista_liczb)
    liczba_liczb = len(lista_liczb)
    return suma / liczba_liczb

print(srednia_liczb([10, 20, 30, 40, 50]))
print(srednia_liczb([11, 20, 33, 40, 50]))
print(srednia_liczb([12, 1110, 15, 430, 540]))
print(srednia_liczb([13, 20, 630, 88, 50]))
print(srednia_liczb([14, 50, 3111, 12, 50]))

# funkcje_03.py

def srednia_liczb_wazona(lista_liczb, wagi=None):
    """
    Funkcja obliczająca ważoną średnią arytmetyczną z listy liczb.
    Jeśli wagi nie są podane, oblicza zwykłą średnią arytmetyczną.
    
    Argumenty:
    - lista_liczb: lista wartości liczbowych.
    - wagi: lista wag dla każdej wartości; domyślnie None, co oznacza równą wagę dla każdej liczby.
    """
    if wagi is None:
        # Jeśli wagi nie są podane, zachowuje się jak zwykła średnia
        return sum(lista_liczb) / len(lista_liczb)
    else:
        # Obliczenie ważonej średniej
        suma_wazona = sum(waga * liczba for waga, liczba in zip(wagi, lista_liczb))
        suma_wag = sum(wagi)
        return suma_wazona / suma_wag

# Przykłady użycia funkcji
wynik_zwykly = srednia_liczb_wazona([10, 20, 30])
wynik_wazony = srednia_liczb_wazona([10, 20, 30], wagi=[1, 2, 3])

print("Zwykła średnia:", wynik_zwykly)
print("Ważona średnia:", wynik_wazony)

# funkcje_04.py

def srednia_liczb_wazona(*lista_liczb, wagi=None):
    """
    Funkcja obliczająca ważoną średnią arytmetyczną z listy liczb.
    Jeśli wagi nie są podane, oblicza zwykłą średnią arytmetyczną.
    
    Argumenty:
    - lista_liczb: lista wartości liczbowych.
    - wagi: lista wag dla każdej wartości; domyślnie None, co oznacza równą wagę dla każdej liczby.
    """
    if wagi is None:
        # Jeśli wagi nie są podane, zachowuje się jak zwykła średnia
        return sum(lista_liczb) / len(lista_liczb)
    else:
        # Obliczenie ważonej średniej
        suma_wazona = sum(waga * liczba for waga, liczba in zip(wagi, lista_liczb))
        suma_wag = sum(wagi)
        return suma_wazona / suma_wag

# Przykłady użycia funkcji
wynik_zwykly = srednia_liczb_wazona(10, 20, 30)
wynik_wazony = srednia_liczb_wazona(10, 20, 30, 40, wagi=[1, 2, 3, 4])

print("Zwykła średnia:", wynik_zwykly)
print("Ważona średnia:", wynik_wazony)