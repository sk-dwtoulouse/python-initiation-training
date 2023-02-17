# Possibilité 1
left = 0
right = 1
new = 1

# Afficher les éléments successifs de la séquence avec une variable new
while new < 10_000:
    new = left + right
    print(new)
    left = right
    right = new


# Possibilité 2
left = 0
right = 1
temp = None

# Afficher les éléments successifs de la séquence avec une variable temporaire
while left + right < 10_000:
    print(left + right)
    temp = left
    left = right
    right = temp + right


# Possibilité 3 : algorithme
left = 0
right = 1

# Afficher les éléments successifs de la séquence sans variable temporaire
while left + right < 10_000:
    print(left + right)
    right = left + right
    left = right - left


# Possibilité 4
left = 0
right = 1

# Afficher les éléments successifs de la séquence via l'unpacking
while left + right < 10_000:
    print(left + right)
    left, right = (right, left + right)
