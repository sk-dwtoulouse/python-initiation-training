# Al et Kim sont inscrits sur un réseau social. Al a les amis suivants :
#
# - Josephine
# - Meghan
# - Amy
# - Bob
#
# Kim a les amis suivants :
#
# - Frank
# - Amy
# - Josephine
# - Susan
#
# Quels sont leurs amis en commun ? Écrivez un code qui représente et résout cet énoncé.
al_friends = {"Josephine", "Meghan", "Amy", "Bob"}
kim_friends = {"Frank", "Amy", "Josephine", "Susan"}

# Afficher le bon résultat
print(al_friends & kim_friends)  # Affichier l'intersection avec des opérateurs
print(al_friends.intersection(kim_friends))  # Affichier l'intersection plus explicite
