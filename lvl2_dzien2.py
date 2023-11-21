# profiling_01.py

import pandas as pd

# Wczytywanie danych
data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Podgląd pierwszych i ostatnich wierszy
print("Pierwsze wiersze danych:")
print(data.head())
print("\nOstatnie wiersze danych:")
print(data.tail())

# Informacje o strukturze i typach danych
print("\nInformacje o danych:")
print(data.info())

# Podstawowe statystyki opisowe
print("\nStatystyki opisowe:")
print(data.describe())

# profiling_02.py

import pandas as pd

# Wczytywanie danych
data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Liczba unikalnych wartości w każdej kolumnie
print("Liczba unikalnych wartości w kolumnach:")
print(data.nunique())

# Liczba unikalnych wartości dla konkretnej kolumny:
print("\nLiczba unikalnych wartości w kolumnie 'GeneID':")
print(data['GeneID'].nunique())

# Unikalne wartości dla konkretnej kolumny:
print("\nUnikalne wartości w kolumnie 'GeneID':")
print(data['GeneID'].unique())

# Liczba brakujących wartości w każdej kolumnie
print("\nLiczba brakujących wartości w kolumnach:")
print(data.isnull().sum())

# Liczba brakujących wartości dla konkretnej kolumny:
print("\nLiczba brakujących wartości w kolumnie 'Control':")
print(data['Control'].isnull().sum())

# profiling_03

import pandas as pd

data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

print("\nStatystyki opisowe:")
print(data.describe())

# Szukamy wartości, których typ nie jest zgodny z typem dominującym w kolumnie.

# Ustalamy dominujący typ danych w kolumnie:
main_data_type = data['TreatmentA'].apply(type).mode().values[0]

# Wyszukujemy komórki, których typ jest inny niż dominujący:
cells_with_different_type = data[data['TreatmentA'].apply(type) != main_data_type]

print(cells_with_different_type)


# profiling_04.py

import pandas as pd

data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Szukamy wartości, których typ nie jest zgodny z typem dominującym w kolumnie.

# Ustalamy dominujący typ danych w kolumnie (rozwinięcie krok po kroku):
# main_data_type = data['TreatmentA'].apply(type).mode().values[0]

# Wybieramy kolumnę 'TreatmentA' z DataFrame i zwraca jej typy danych:
tA_column = data['TreatmentA']
data_types = tA_column.apply(type)
print(data_types)

# Dodatkowo, możemy sprawdzić, jakie typy danych występują w kolumnie 'TreatmentA':
print(data_types.unique())

# Możemy też sprawdzić, ile razy występuje każdy typ danych:
print(data_types.value_counts())

# Znajdujemy najczęściej występujący typ danych w kolumnie 'TreatmentA'.
# .mode() zwraca Series, czyli, technicznie, sekwencję wartości.
# W praktyce jest to DataFrame z jedną kolumną i jednym wierszem.
# Aby uzyskać wartość z tej komórki, możemy użyć .values[0]:
main_data_type_series = data_types.mode()
main_data_type = main_data_type_series.values[0]
print(main_data_type)


# Wyszukujemy komórki, których typ jest inny niż dominujący (rozwinięcie krok po kroku):
cells_with_different_type = data[data_types != main_data_type]

print(cells_with_different_type)

# profiling_05.py

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Wykresy pudełkowe dla każdej kolumny numerycznej
data.plot(kind='box')
plt.title('Wykresy pudełkowe dla kolumn numerycznych')
plt.show()

# Histogram dla konkretnej kolumny
data['TreatmentB'].hist()
plt.title('Histogram kolumny')
plt.show()

# Wykres słupkowy dla brakujących danych
data.isnull().sum().plot(kind='bar')
plt.title('Brakujące dane w każdej kolumnie')
plt.show()


# cleaning_01.py

import pandas as pd

data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Zamiana wartości w kolumnie 'TreatmentA' na typ float "na siłę", tzn.
# jeśli wartość nie jest liczbą, to zostanie zamieniona na NaN.
data['TreatmentA'] = pd.to_numeric(data['TreatmentA'], errors='coerce')

# cleaning_02.py

import pandas as pd

data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Ustalamy listę komórek z wartościami, które nie są typu float:
main_data_type = data['TreatmentA'].apply(type).mode().values[0]
cells_with_different_type = data[data['TreatmentA'].apply(type) != main_data_type]
print(cells_with_different_type)

# Wynik (3 komórki o indeksach 35, 38 i 50):
#         GeneID   Control         TreatmentA  TreatmentB ExperimentDate
# 35  Gene_00036  8.086137   10.242918526454'    5.224108     2023-01-07
# 38  Gene_00039       NaN  11.6905220055877'    7.700813     2023-01-02
# 50  Gene_00051  6.985808              error    4.929958     2023-01-19

# Zauważmy, że w komórkach 35 i 38 wartości są poprzedzone znakiem '.
# Możemy usunąć ten znak i przekształcić wartości na float.
data.at[35, 'TreatmentA'] = data.at[35, 'TreatmentA'].replace("'", "")
data.at[35, 'TreatmentA'] = float(data.at[35, 'TreatmentA'])

data.at[38, 'TreatmentA'] = data.at[38, 'TreatmentA'].replace("'", "")
data.at[38, 'TreatmentA'] = float(data.at[38, 'TreatmentA'])

# data.at[35, 'TreatmentA'] = 1.0
# data.at[38, 'TreatmentA'] = 2.0
# data.at[50, 'TreatmentA'] = 2.0
# Wartość 'error' w komórce 50 jest trudna do przekształcenia na float.
# Możemy usunąć cały wiersz, jeśli nie jest nam potrzebny.
# inplace=True oznacza, że zmiany będą dokonane na obiekcie data. (bez przypisania do nowej zmiennej)
data.drop([50], inplace=True)

# W DataFrame kolumna TreatmentA nadal ma przypisany typ "object".
# Zmieniamy typ na float:
data['TreatmentA'] = pd.to_numeric(data['TreatmentA'])

print(data.info())

# cleaning_03.py

import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Ujednolicanie typów danych w kolumnie 'TreatmentA':

data.at[35, 'TreatmentA'] = data.at[35, 'TreatmentA'].replace("'", "")
data.at[35, 'TreatmentA'] = float(data.at[35, 'TreatmentA'])
data.at[38, 'TreatmentA'] = data.at[38, 'TreatmentA'].replace("'", "")
data.at[38, 'TreatmentA'] = float(data.at[38, 'TreatmentA'])
data.drop([50], inplace=True)
data['TreatmentA'] = pd.to_numeric(data['TreatmentA'])

# Pozbywanie się duplikatów:
data.drop_duplicates(inplace=True)

# Usuwanie brakujących wartości:
data.dropna(inplace=True)

# Analiza wyczyszczonego DataFrame:
print(data.info())

data.plot(kind='box')
plt.title('Wykresy pudełkowe dla kolumn numerycznych')
plt.show()

# cleaning_04.py

import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Ujednolicanie typów danych w kolumnie 'TreatmentA':

data.at[35, 'TreatmentA'] = data.at[35, 'TreatmentA'].replace("'", "")
data.at[35, 'TreatmentA'] = float(data.at[35, 'TreatmentA'])
data.at[38, 'TreatmentA'] = data.at[38, 'TreatmentA'].replace("'", "")
data.at[38, 'TreatmentA'] = float(data.at[38, 'TreatmentA'])
data.drop([50], inplace=True)
data['TreatmentA'] = pd.to_numeric(data['TreatmentA'])

# Pozbywanie się duplikatów:
data.drop_duplicates(inplace=True)

# Usuwanie brakujących wartości:
data.dropna(inplace=True)

# Pozbywanie się wartości odstających:
data.drop(data[data['TreatmentB'] > 25].index, inplace=True)

# Analiza wyczyszczonego DataFrame:
print(data.info())

data.plot(kind='box')
plt.title('Wykresy pudełkowe dla kolumn numerycznych')
plt.show()

# saving_01.py

import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_excel('synthetic_gene_expression_data_2023.xlsx')

# Ujednolicanie typów danych w kolumnie 'TreatmentA':

data.at[35, 'TreatmentA'] = data.at[35, 'TreatmentA'].replace("'", "")
data.at[35, 'TreatmentA'] = float(data.at[35, 'TreatmentA'])
data.at[38, 'TreatmentA'] = data.at[38, 'TreatmentA'].replace("'", "")
data.at[38, 'TreatmentA'] = float(data.at[38, 'TreatmentA'])
data.drop([50], inplace=True)
data['TreatmentA'] = pd.to_numeric(data['TreatmentA'])

# Pozbywanie się duplikatów:
data.drop_duplicates(inplace=True)

# Usuwanie brakujących wartości:
data.dropna(inplace=True)

# Pozbywanie się wartości odstających:
data.drop(data[data['TreatmentB'] > 25].index, inplace=True)

# Zapis do pliku excela:
data.to_excel('cleaned_data.xlsx', index=False)

