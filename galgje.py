import random
def spel():
  turns = 10

    
  def drawgalgjes():
    if turns == 9:
        print("""  
        |
        |
        |
        |
        |
    _____|""")

    if turns == 8:
        print("""  ____
        |
        |
        |
        |
        |
    _____|""")

    if turns == 7:
        print("""  ____
        \|
        |
        |
        |
        |
    _____|""")

    if turns == 6:
        print("""  ____
      | \|
        |
        |
        |
        |
    _____|""")

    if turns == 5:
        print("""  ____
      | \|
      o  |
        |
        |
        |
    _____|""")

    if turns == 4:
        print("""  ____
      | \|
      o  |
      |  |
        |
        |
    _____|""")

    if turns == 3:
        print("""  ____
      | \|
      o  |
    /|\  |
        |
        |
    _____|""")

    if turns == 2:
        print("""  ____
      | \|
      o  |
    /|\ |
    / \ |
        |
    _____|""")

    if turns == 1:

        print("Je hebt het woord", hetwoord, "niet kunnen raden, volgende keer beter!")
        exit();
    


  woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", 
  "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]



  hetwoord= random.choice(woordenlijst)
  lengtewoord = len(hetwoord)
  puntjes = ["_ "] * lengtewoord


  naam = input("vul hier je naam in: ")
  print()
  print("Welkom", naam,"bij ons galgje spel")
  game = True

  print("Raad de letters en als je het woord weet typ het dan in.")
  print()
  print("het woord heeft " + str(lengtewoord) + " letters")
  print(puntjes)



  while game == True:
    userGuess = input("geef letter> ")
    #zit letter in woord? Zo ja, waar dan?
    if userGuess == hetwoord:
      print ("gewonnen")
      spel()
    else:
      if userGuess in hetwoord:
        for idx, letter in enumerate(hetwoord):
          
          if(letter == userGuess):
            puntjes[idx] = userGuess

      #zo niet, beurt eraf en galgjes tekenen
      else:
        turns -= 1
        drawgalgjes()

    print(''.join(puntjes))



  guessed = ""

  missed = 1


  if puntjes == hetwoord:
      print(hetwoord)
      print("je hebt het woord", hetwoord, "geraden")

  gokje = input()


  if gokje not in letters:
    print("vul een geldig woord in")

    gokje = input()

    if guess not in word:
      turns = turns - 1
    
spel()
