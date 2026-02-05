# Zadanie: Masz plik raw.txt, który zawiera puste i niepuste linie.
# Napisz program, który:
# odczytuje wszystkie linie z raw.txt
# usuwa puste linie (linie, które są puste lub zawierają tylko białe znaki)
# zapisuje tylko niepuste linie do nowego pliku o nazwie clean.txt
# Wskazówka: Użyj .strip() aby sprawdzić czy linia jest pusta; if line.strip() != "", zachowaj ją.
# Odczytujemy wszystkie linie z pliku raw.txt
with open("raw.txt", "r") as file:
    lines = file.readlines()
    non_empty_lines = [line for line in lines if line.strip() != ""]
with open("clean.txt", "w") as file:
    file.writelines(non_empty_lines)
