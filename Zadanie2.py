# Zapytaj u¿ytkownika o nazwisko
name = input("Name?: ")
# Zapytaj u¿ytkownika o wiek
age = input("Age?: ")
# Zapytaj u¿ytkownika o miasto
city = input("City?: ")
# Zapytaj u¿ytkownika o jego zainteresowania
interest = input("Interest?: ")
# Utwórz tekst wyjœciowy za pomoc¹ formatowania ci¹gów
string = "Hi {}, you are {} years old. You live in {} and you love {}!"
output = string.format(name,age,city,interest)
# Wydrukuj tekst wyjœciowy
print(output)
