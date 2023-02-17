# Créer des ensembles avec au moins deux valeurs en commun
set1 = {2, 4, 6, 8, 10}
set2 = {8, 10, 12, 14, 16}

# Tenter d'ajouter une valeur déjà présente dans set1
set1.add(6)

# Afficher l'intersection des deux ensembles (valeurs en commun)
print(set1 & set2)  # c'est pareil mais moins explicite
print(set1.intersection(set2))  # c'est pareil mais plus explicite

# Afficher l'union des deux ensembles (toutes valeurs)
print(set1 | set2)
print(set1.union(set2))

