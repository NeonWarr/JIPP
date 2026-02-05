# Użyj modułu random
import random

# Stwórz listę "questions" składającą się z 3 pytań, które często zadają dzieci
questions = ["Why is the sky blue? ","Why is the sun round? ","Where are all the dinosaurs? "]

# Wybierz losowe pytanie z danej listy za pomocą instrukcji warunkowej
question = random.choice(questions)

# Zadaj wybrane pytanie za pomocą funkcji input()
answer = input(question)

# Pytania muszą zachować jednolite formatowanie
# Aby to uzyskać, przekonwertuj wszystkie odpowiedzi na małe litery i usuń wszelkie nadmiarowe spacje
answer = answer.strip().lower()

# Poczekaj do czasu, aż użytkownik wprowadzi hasło "To wszystko"
while answer != "to wszystko":
    question = random.choice(questions)
    answer = input(question).strip().lower()

# Wyświetl wiadomość
print("\nRodzic mówi: Basta! Koniec tych pytań.")