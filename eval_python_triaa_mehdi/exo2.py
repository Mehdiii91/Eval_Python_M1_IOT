def addition_listes(n1, n2):
    resultat = []
    retenue = 0
    i, j = len(n1) - 1, len(n2) - 1
    
    while i >= 0 or j >= 0 or retenue:
        somme = retenue
        if i >= 0:
            somme += n1[i]
            i -= 1
        if j >= 0:
            somme += n2[j]
            j -= 1
        
        resultat.insert(0, somme % 10)
        retenue = somme // 10
    
    return resultat

# Exemple d'utilisation
print(addition_listes([1, 2, 3], [7]))  
print(addition_listes([8, 4, 0], [8, 3]))  
print(addition_listes([1, 8, 3], [7]))  