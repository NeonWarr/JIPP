#Zadanie: Napisz program, który:
#pyta użytkownika o jego imię i wiek
#zapisuje dane do user.txt w tym formacie:
#Imię: Jan Wiek: 12
#Wskazówka: Użyj input() aby odczytać dane od użytkownika, i write() aby formatować tekst za pomocą f-stringów.
def main():
    imie = input("Podaj swoje imię: ")
    wiek = input("Podaj swój wiek: ")
    with open("user.txt", "w") as file:
        file.write(f"Imię: {imie} Wiek: {wiek}\n")
    with open("user.txt", "r") as file:
        zawartosc = file.read()
        print("Zawartość pliku user.txt:")
        print(zawartosc)
        if __name__ == "__main__":
            main()
main()

