# cwiczenie_01.py

import pandas as pd
import matplotlib.pyplot as plt

# 1. Za pomocą pandas, pobierz dane z pliku bialka_sekwencje.xlsx
# 2. Dla każdej rodziny sekwencji białkowych (dane syntetyczne) oblicz
#   - średnią długość sekwencji
#   - średnią liczbę cystein ("C") w sekwencjach
# 3. Dla każdej z policzonych wartości stwórz:
#   - opis wyników w konsoli, z wykorzystaniem f-stringów
#   - wizualizację w postaci wykresu słupkowego

data = pd.read_excel("bialka_sekwencje.xlsx")

family_data = {}

for index, row in data.iterrows():
    family_id = row["family"]
    sequence = row["sequence"]

    if family_id not in family_data:
        family_data[family_id] = {
            "sequences_count": 1,
            "sequence_length": len(sequence),
            "cysteine_count": sequence.count("C"),
        }
    else:
        family_data[family_id]["sequences_count"] += 1
        family_data[family_id]["sequence_length"] += len(sequence)
        family_data[family_id]["cysteine_count"] += sequence.count("C")

family_ids = []
avg_lengths = []
avg_cysteine_counts = []

for key in family_data:
    family_ids.append(key)
    avg_lengths.append(family_data[key]["sequence_length"] / family_data[key]["sequences_count"])
    avg_cysteine_counts.append(family_data[key]["cysteine_count"] / family_data[key]["sequences_count"])
    print(f"Rodzina {key}: średnia długość sekwencji: {avg_lengths[-1]:.2f}, średnia zawartość cystein: {avg_cysteine_counts[-1]:.2f}")

plt.figure(figsize=(10, 5))
plt.bar(family_ids, avg_lengths)
plt.xlabel("Rodzina")
plt.ylabel("Średnia długość sekwencji")
plt.title("Średnia długość sekwencji w zależności od rodziny")
plt.xticks(family_ids)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(family_ids, avg_cysteine_counts)
plt.xlabel("Rodzina")
plt.ylabel("Średnia zawartość cystein")
plt.title("Średnia zawartość cystein w sekwencjach w zależności od rodziny")
plt.xticks(family_ids)
plt.show()


# cwiczenie_02.py

import pandas as pd
import matplotlib.pyplot as plt

# Zmodyfikuj funkcję srednia_liczb_wazona() tak, 
# żeby liczba podanych w drugim argumencie wag, 
# musiała być równa liczbie podanych w pierwszym argumencie liczb 
# (na przykład: wyświetl komunikat w przypadku niezgodności).


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
    elif len(lista_liczb) != len(wagi):
        # Jeśli liczba wag jest różna od liczby liczb, wyświetl komunikat
        print("Liczba wag musi być równa liczbie liczb!")
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


# zadanie_domowe_01.py

import pandas as pd
import matplotlib.pyplot as plt

def analyze_sequences(file_path, amino_acid, bar_color):
    data = pd.read_excel(file_path)
    
    # Słownik, w którym będą przechowywane informacje o każdej z rodzin
    family_data = {}

    # Iterowanie po wierszach w DataFrame
    for index, row in data.iterrows():
        family_id = row["family"]
        sequence = row["sequence"]

        # Jeżeli rodziny nie ma w słowniku, dodaj ją
        if family_id not in family_data:
            family_data[family_id] = {
                "sequences_count": 1,
                "sequence_length": len(sequence),
                amino_acid + "_count": sequence.count(amino_acid),
            }
        # W innym przypadku zwiększ liczbę sekwencji i długość sekwencji
        else:
            family_data[family_id]["sequences_count"] += 1
            family_data[family_id]["sequence_length"] += len(sequence)
            family_data[family_id][amino_acid + "_count"] += sequence.count(amino_acid)

    # Inicjalizacja list, do których będą dodawane dane do wykresów
    family_ids = []
    avg_lengths = []
    avg_aa_counts = []

    # Liczenie średniej długości sekwencji i średniej zawartości aminokwasu
    for key in family_data:
        family_ids.append(key)
        avg_lengths.append(family_data[key]["sequence_length"] / family_data[key]["sequences_count"])
        avg_aa_counts.append(family_data[key][amino_acid + "_count"] / family_data[key]["sequences_count"])
        print(f"Rodzina {key}: średnia długość sekwencji: {avg_lengths[-1]:.2f}, średnia zawartość {amino_acid}: {avg_aa_counts[-1]:.2f}")

    # Tworzenie wykresów słupkowych (średnia długość sekwencji i średnia zawartość aminokwasu)
    plt.figure(figsize=(10, 5))
    plt.bar(family_ids, avg_lengths, color=bar_color)
    plt.xlabel("Rodzina")
    plt.ylabel("Średnia długość sekwencji")
    plt.title(f"Średnia długość sekwencji w zależności od rodziny - {amino_acid}")
    plt.xticks(family_ids)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(family_ids, avg_aa_counts, color=bar_color)
    plt.xlabel("Rodzina")
    plt.ylabel(f"Średnia zawartość {amino_acid}")
    plt.title(f"Średnia zawartość {amino_acid} w sekwencjach w zależności od rodziny")
    plt.xticks(family_ids)
    plt.show()

analyze_sequences("bialka_sekwencje.xlsx", "C", "green")

# zadanie_domowe_02.py

import matplotlib.pyplot as plt


def plot_dna_base_frequency(fasta_file):
    """
    Funkcja przyjmuje plik tekstowy w formacie FASTA zawierający sekwencję DNA.
    Następnie tworzy wykres słupkowy, gdzie każdy słupek reprezentuje liczbę wystąpień
    konkretnej zasady azotowej i jest innego koloru.
    """

    # Wczytaj plik FASTA i zainicjalizuj zmienną do przechowywania sekwencji
    with open(fasta_file, 'r') as file:
        sequence = ''
        for line in file:
            # Pomijamy linie nagłówkowe rozpoczynające się od '>'
            if not line.startswith('>'):
                sequence += line.strip()  # Usuwamy znaki końca linii i dodajemy do sekwencji

    # Zlicz wystąpienia każdej zasady
    base_counts = {'A': sequence.count('A'),
                   'C': sequence.count('C'),
                   'G': sequence.count('G'),
                   'T': sequence.count('T')}

    # Kolory dla słupków
    colors = ['red', 'blue', 'green', 'yellow']

    # Tworzenie wykresu
    plt.figure(figsize=(10, 5))
    plt.bar(base_counts.keys(), base_counts.values(), color=colors)
    plt.title('Liczba wystąpień zasad azotowych w sekwencji DNA')
    plt.xlabel('Zasada azotowa')
    plt.ylabel('Liczba wystąpień')
    plt.show()

# Aby użyć funkcji, podajemy ścieżkę do pliku FASTA:
plot_dna_base_frequency('seq1.fasta')
