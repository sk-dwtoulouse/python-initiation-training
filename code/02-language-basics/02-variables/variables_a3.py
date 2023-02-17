saisie1 = input("Entrez un premier nombre :")
saisie2 = input("Entrez un second nombre :")
# Convertir les deux entrées en entiers pour pouvoir les comparer
saisie1 = float(saisie1)
saisie2 = float(saisie2)

# Afficher le nombre le plus grand, nécessite d'avoir vu les conditions
if saisie1 > saisie2:
    print(saisie1, "est le plus grand nombre")
else:
    print(saisie2, "est le plus grand nombre")
