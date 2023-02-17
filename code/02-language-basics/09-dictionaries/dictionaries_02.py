# - Écrivez un simple dictionnaire associant des noms à des âges :
# * Paul → 30
# * Karim → 22
# * Gina → 41
# * Anna → 25
# - Affichez l'âge de Gina
# - Ajoutez les associations suivantes :
# * Alina → 33
# * Victor → 55
# - Affichez le contenu du dictionnaire
ages = {"Paul": 30, "Karim": 22, "Gina": 41, "Anna": 25}
ages["Victor"] = 55
ages["Alina"] = 33

# Parcourir les clés et afficher la valeur associée
for name in ages:
    print(name)
    print(ages[name])
