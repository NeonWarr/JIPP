#Zadanie: Masz listę:
#words = ["jabłko", "banan", "wiśnia"]
#Napisz program, który zapisuje tę listę do pliku o nazwie fruits.txt tak, aby każde słowo było w osobnej linii.
#Wskazówka: Iteruj po liście i użyj file.write() z "\n". Lub użyj "\n".join(lista).

words = ["jabłko", "banan", "wiśnia"]
with open("fruits.txt", "w", encoding="utf-8") as file:
    for word in words:
        file.write(word + "\n")
