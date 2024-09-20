def separer_phrase(phrase):
    mots = []
    separateurs = []
    mot = ""
    
    for caractere in phrase:
        if caractere.isalnum() or caractere in ["'", "-"]:
            mot += caractere
        else:
            if mot:
                mots.append(mot)
                mot = ""
            separateurs.append(caractere)
    
    if mot:
        mots.append(mot)
    
    return [mots, separateurs]

# Exemple d'utilisation
print(separer_phrase("J'ai découvert Python cette semaine"))
print(separer_phrase("J'ai découvert, Python, cette semaine"))
