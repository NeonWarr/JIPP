# Zadanie: Napisz program, który:
# odczytuje zawartość numbers.txt
# kopiuje wszystko do nowego pliku o nazwie copy.txt
# Wskazówka: Użyj read() aby pobrać całą zawartość na raz, lub kopiuj linię po linii.
with open('numbers.txt', 'r') as source_file:
    content = source_file.read()
with open('copy.txt', 'w') as dest_file:
    dest_file.write(content)
print("Zawartość została skopiowana z numbers.txt do copy.txt")
