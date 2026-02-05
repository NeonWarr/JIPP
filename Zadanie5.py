# Utwórz słownik filmów. Niech  kluczem będzie nazwa filmu, a parą wartości dwie liczby: kryteria wiekowe oraz liczba dostępnych biletów
movies = {"Finding Nemo":[5,2], "Moana":[6,3], "Batman":[18,5], "The Lion King":[10,4]}
# Utwórz pętlę, która będzie działać w nieskończoność
while True:
    # Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca a następnie zamień frazę na format tytułowy (pierwsza litera każdego słowa jest wielka)
    selected_movie = input("Wybierz film (lub wpisz 'exit' aby zakończyć): ").strip().title()
    # Stwórz instrukcję warunkową if. Jeśli wybrany film jest odostępny w słowniku, kontynuuj
    if selected_movie == 'Exit':
        break
    if selected_movie in movies:
        # Zapytaj użytkownika o wiek
        user_age = int(input("Podaj swój wiek: "))
        # Sprawdź użytkownika pod kątem kwalifikowalności
        age_limit = movies[selected_movie][0]
        if user_age >= age_limit:
            # Jeśli użytkownik znajduje się w grupie docelowej, sprawdź dostępność miejsc
            available_seats = movies[selected_movie][1]
            # Jeśli liczba dostępnych miejsc jest wartością dodatnią, zmiejsz pulę dostępnych miejsc o 1
            if available_seats > 0:
                movies[selected_movie][1] -= 1
                print("Bilet zakupiony pomyślnie na film:", selected_movie)
            else:
                print("Niestety, brak dostępnych miejsc na ten film.")
        else:
            print("Niestety, nie spełniasz wymagań wiekowych dla tego filmu.")
    else:
        print("Film nie znaleziony w ofercie.")
