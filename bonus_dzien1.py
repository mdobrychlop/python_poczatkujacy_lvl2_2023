# Pierwszy dzien szkolenia - materialy dodatkowe.

# Bonus 1: Argumenty funkcji (pozycyjne, nazwane, domyslne, *args, **kwargs)

# Argumenty pozycyjne:
# Argumenty pozycyjne są najczęstszym rodzajem argumentów w funkcjach Pythona. 
# Są przekazywane do funkcji na podstawie ich pozycji w wywołaniu funkcji.

def przywitaj(imie, powitanie):
    return f"{powitanie}, {imie}!"

wynik = przywitaj("Alicja", "Cześć")
print(wynik)  # Wynik: "Cześć, Alicja!"

# Argumenty nazwane i wartości domyślne:
# Możesz również użyć argumentów nazwanych, aby określić, 
# którego argumentu dotyczy przekazywana wartość. To może uczynić Twój kod bardziej czytelnym.
# W takim wypadku niezawsze jest konieczne przekazywanie argumentów w określonej kolejności.
# Możesz również ustawić wartości domyślne dla argumentów, które nie są przekazywane do funkcji.
# (w przykładzie poniżej, domyślną wartością argumentu powitanie jest "Cześć")

def przywitaj(imie, powitanie="Cześć"):
    return f"{powitanie}, {imie}!"

wynik = przywitaj(powitanie="Hej", imie="Alicja")  # Używanie argumentów słownikowych
print(wynik)  # Wynik: "Hej, Alicja!"

# Argumenty *args:
# Czasami nie wiesz, ile argumentów zostanie przekazanych do funkcji.
# W takim przypadku możesz użyć *args jako argumentu funkcji.

def przywitaj(*args):
    return f"Cześć, {', '.join(args)}!"

wynik = przywitaj("Alicja", "Bob", "Cecylia")
print(wynik)  # Wynik: "Cześć, Alicja, Bob, Cecylia!"

# Argumenty **kwargs:
# Możesz również użyć **kwargs jako argumentu funkcji,
# jeśli nie wiesz, ile argumentów nazwanych zostanie przekazanych do funkcji.

def drukuj_info(**kwargs):
    for klucz, wartosc in kwargs.items():
        print(f"{klucz}: {wartosc}")

drukuj_info(imie="Alicja", wiek=30, miasto="Nowy Jork")  # Pozwala na dowolne argumenty nazwane
# Wynik:
# imie: Alicja
# wiek: 30
# miasto: Nowy Jork

# Kolejność argumentów:
# W Pythonie argumenty pozycyjne muszą być przekazywane przed argumentami nazwanymi.
# Argumenty *args muszą być przekazywane przed argumentami **kwargs.

# Bonus 2: Wykresy słupkowe w matplotlib - dodatkowe przykłady.

# Przykład 1 - kolory słupków:

import matplotlib.pyplot as plt 

# Dane do wykresu
zwierzeta = ['Kot', 'Pies', 'Słoń', 'Wilk']
ilosc = [20, 45, 35, 10]

# Tworzenie wykresu słupkowego
plt.bar(zwierzeta, ilosc, color='green')  # Zmiana koloru słupków na zielony
# Kolory przekazywane w argumencie color mogą być podane jako nazwa koloru lub kod szesnastkowy.
# Na przykład: color='green' lub color='#00FF00'
# Przykkładowe nazwy kolorów: https://matplotlib.org/stable/gallery/color/named_colors.html

# Modyfikacja etykiet
plt.xlabel('Zwierzęta')
plt.ylabel('Ilość')
plt.title('Ilość zwierząt w zoo')

# Wyświetlenie wykresu
plt.show()

# Przykład 2 - adnotacja na wykresie:

import matplotlib.pyplot as plt

# Dane dotyczące liczby różnych gatunków ptaków
gatunki = ['Kanarek', 'Sójka', 'Kruk', 'Papuga', 'Sokół']
liczba_ptakow = [100, 50, 70, 10, 30]

plt.bar(gatunki, liczba_ptakow, color='green')
plt.xlabel('Gatunki ptaków')
plt.ylabel('Liczba ptaków')
plt.title('Liczba ptaków różnych gatunków')
plt.ylim(0, 150)  # Ustalamy zakres osi y
plt.annotate('Najwięcej', xy=(0.6, 100), xytext=(0.8, 120),
             arrowprops={'arrowstyle': '->', 'color': 'blue'})
plt.show()

# Przykład 3 - wykres z dwiema seriami danych:

import matplotlib.pyplot as plt

# Dane dotyczące liczby ssaków i ptaków w różnych regionach
regiony = ['Afryka', 'Azja', 'Ameryka Południowa', 'Europa', 'Australia']
liczba_ssakow = [2000, 3000, 1500, 2500, 1000]
liczba_ptakow = [1000, 1500, 800, 1200, 500]

x = range(len(regiony))

szerokosc_slupka = 0.35

plt.bar([i - szerokosc_slupka/2 for i in x], liczba_ssakow, szerokosc_slupka, label='Ssaki', color='orange')
plt.bar([i + szerokosc_slupka/2 for i in x], liczba_ptakow, szerokosc_slupka, label='Ptaki', color='blue')
plt.xlabel('Regiony')
plt.ylabel('Liczba gatunków')
plt.title('Liczba gatunków ssaków i ptaków w różnych regionach')
plt.xticks(x, regiony, rotation=45)
plt.legend()
plt.show()


