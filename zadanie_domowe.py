bazadanych = []

while True:
   x=input(" 1.Dodaj użytkownika \n 2.Zobacz dane użykownika \n 3.Wyświetl wszystkie imiona użytkowników \n 4.Zakończ dziłanie programu")

   if x=="1":
       imie = input("podaj imie:")
       email = input("podaj adres email:")
       wiek = input("podaj swój wiek:")
       uzytkownik={
           "imie":imie,
           "email":email,
           "wiek":wiek}
       bazadanych.append(uzytkownik)

   elif x=="2":
        login = input("podaj imie użytkownika:")
        for y in bazadanych:
            if y["imie"] == login:
                        print(y)
            elif y["imie"] != login:
                print("!brak uzytkownika o podanym imieniu!")

   elif x=="3":
       if len(bazadanych) == 0:
           print("!brak uzytkownikow!")
       for y in bazadanych:
           print(y["imie"])

   elif x=="4":
       print("!wychodze!")
       break

   else:
       print("!źle wprowadzone dane!")

