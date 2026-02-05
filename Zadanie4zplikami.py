# Zadanie: Masz plik numbers.txt z jedną liczbą w każdej linii, na przykład:
# 10 3 7 -2
# Napisz program, który:
# odczytuje liczby z pliku
# konwertuje je na int
# oblicza ich sumę
# wyświetla wynik
# Wskazówka: Użyj int(line.strip()) i przechowuj bieżącą sumę w zmiennej.
filename = 'numbers.txt'
def sum_numbers_from_file(filename):
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                total_sum += number
        print(f"Suma liczb w pliku '{filename}' wynosi: {total_sum}")
    except FileNotFoundError:
        print(f"Plik '{filename}' nie został znaleziony.")
sum_numbers_from_file(filename)