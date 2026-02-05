# Utwórz zmienne "vowels" (samogłoski) i "consonants" (spółgłoski) i przypisz każdej z nich wartość 0
vowels = 0
consonants = 0
# Utwórz pętlę i przeiteruj łańcuch znaków „Programowanie Pythona”
# Utwórz instrukcję warunkową IF-ELSE, która wyliczy liczbę samogłosek i spółgłosek w danym łańcuchu znaków
string = "Programowanie Pythona"
for char in string.lower():
    if char in "aeiouąęioóuy":
        vowels += 1
    elif char.isalpha():
        consonants += 1
# Wydrukuj łączną liczbę samogłosek i spółgłosek w danym łańcuchu znaków
print("Liczba samogłosek:", vowels)
print("Liczba spółgłosek:", consonants)





    
        

