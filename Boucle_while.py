# Teste jeu 
# Option Propose a l'utilisateur:  - tant qu'il choisie de continué la boucle du jeux continue - si le user choisie la salutation 'Bonjour lui sera affiche' - si le user choisi de quitter la boucle s'arrete 

start_game = True

print("BIENVENU  SUR LE WIKI-PYTHON-GAME-THAT-NEVER-END ")
print("eNTRE VOTRE GAMER_NAME")
gamer_name = input('> ')

while start_game:
    
    print("quelle est ton choix : continue , quitter , say_bonjour")

    choix = input("Vote choix >")
    if choix == "continue":
      continue
    elif choix == "quitter":
      start_game = False
    elif choix == "say_bonjour":
      print("BONJOUR CHER GAME_USER", gamer_name)
      break

print("A BIENTOT...")
