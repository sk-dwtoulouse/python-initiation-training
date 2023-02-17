is_on = True
saisie = input("Saisissez une commande (Marche ou Arrêt) :")

if saisie == "Marche":
    if is_on is False:
        print("Allumage en cours…")
    else:
        print("Déjà allumé !")
elif saisie == "Arrêt":
    if is_on:
        print("Extinction…")
    else:
        print("Déjà éteint !")
