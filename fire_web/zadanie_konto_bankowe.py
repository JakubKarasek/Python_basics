x = input("Imię: ")
y = input("Hasło: ")
z = 2130

while True:
  if x == "Arnold" and y == "icra2013":
      print ("Saldo: ", z)
      print("Jaką czynność chcesz wykonać?\nA - wpłata\nB - wypłata")
      czynnosc = input("Czynność: ")
      if czynnosc == "A":
          wplata = int(input("Podaj kwotę: "))
          if wplata > 0:
              z += wplata
              print("Twoje saldo wynosi teraz: ", z)
              break
          else:
              print("Błędna kwota")
              break
      elif czynnosc == "B":
          wyplata = int(input("Podaj kwotę: "))
          if wyplata < z:
              z -= wyplata
              print("Twoje saldo wynosi teraz: ", z)
              break
          else:
              print("Idź do pracy!")
              break
  else:
      print("Błędne dane")
      break





















































