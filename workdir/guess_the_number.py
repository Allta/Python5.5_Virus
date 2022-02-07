#!/usr/bin/env python3.10
from random import randrange

def difficulty(lvl):
  match lvl:
    case 5:
      return  5
    case 10:
     return  10
    case 15:
      return  15
    case _:
      return  20
      
   

def game():
  to_guess = (randrange(10))
  while True:
    try:
      lvl=input("Entrez le niveau de difficulte  [5/10/15] : ")
      lvl=int(lvl)
      if(lvl == 5) or (lvl == 10) or (lvl == 15):
        nb_try=difficulty(lvl)
        break
      print("Veuillez rentrez un nombre valide")
      continue
    except ValueError:
      print("Veuillez renseigner un nombre")
      continue
  print(f"Vous avez {nb_try} essais")
  while nb_try > 0:
    while True:
      try:
        nb = int(input("Veuillez rentrer un nombre : "))
        break
      except ValueError:
        print("Veuillez renseigner un nombre")
        continue
       
    if(nb == to_guess):
      print("Felicitations")
      again = input("Try again ? [y/n] ")
      if again == "y":       
        game()
      else:
        exit()
    elif(nb > to_guess):
      print("Trop haut")
    elif(nb < to_guess):
      print("Trop bas")
    nb_try -= 1
    print(f"Il vous reste {nb_try}")

game()
