def deviner_nombre():
    bas, haut = 1, 100
    essais = 0
    proposition_precedente = None
    direction_precedente = None

    while True:
        essais += 1
        proposition = (bas + haut) // 2
        
        reponse = input(f"Le script propose {proposition}. Plus (+), Moins (-) ou Gagné (G) ? ").strip().lower()

        # Vérification de la triche
        if proposition_precedente is not None:
            if direction_precedente == "+" and proposition <= proposition_precedente:
                print(f"Tricheur !!! Vous avez dit que le nombre était plus grand que {proposition_precedente}, mais maintenant vous dites qu'il est plus petit ou égal.")
                break
            elif direction_precedente == "-" and proposition >= proposition_precedente:
                print(f"Tricheur !!! Vous avez dit que le nombre était plus petit que {proposition_precedente}, mais maintenant vous dites qu'il est plus grand ou égal.")
                break

        if reponse == "+":
            bas = proposition + 1
            direction_precedente = "+"
        elif reponse == "-":
            haut = proposition - 1
            direction_precedente = "-"
        elif reponse == "g":
            print(f"Le script a trouvé {proposition} en {essais} coups!")
            break
        else:
            print("Réponse invalide.")
            continue

        # Sauvegarder la proposition actuelle pour la vérification de la prochaine étape
        proposition_precedente = proposition

# Exemple d'utilisation
deviner_nombre()
