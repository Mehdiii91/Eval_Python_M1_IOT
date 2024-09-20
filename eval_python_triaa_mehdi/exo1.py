def trouver_triplets(liste):
    resultat = []
    liste.sort()  # Tri de la liste
    for i in range(len(liste) - 2):
        if i > 0 and liste[i] == liste[i - 1]:
            continue
        gauche, droite = i + 1, len(liste) - 1
        while gauche < droite:
            somme = liste[i] + liste[gauche] + liste[droite]
            if somme == 0:
                resultat.append([liste[i], liste[gauche], liste[droite]])
                gauche += 1
                droite -= 1
                while gauche < droite and liste[gauche] == liste[gauche - 1]:
                    gauche += 1
            elif somme < 0:
                gauche += 1
            else:
                droite -= 1
    return resultat

# Exemple d'utilisation
print(trouver_triplets([2, 7, 9, -9]))
print(trouver_triplets([-33, -10, -8, -2, 1, 4, 9, 10]))
print(trouver_triplets([1, 2, -3, 10]))
print(trouver_triplets([1, 2, 3, 10]))