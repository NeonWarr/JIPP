#Zadanie: Napisz program, który:
#odczytuje plik o nazwie story.txt
#liczy ile słów znajduje się w pliku ignoruj puste linie
#wyświetla wynik, np.: "Liczba słów: 42"
#Wskazówka: Użyj read() lub pętli po liniach; podziel tekst używając .split() aby uzyskać słowa.

with open('story.txt', 'r', encoding='utf-8') as file:
    word_count = 0
    for line in file:
        stripped_line = line.strip()
        if stripped_line:
            words = stripped_line.split()
            word_count += len(words)
print("Liczba słów:", word_count)

