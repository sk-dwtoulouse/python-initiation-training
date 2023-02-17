# Nombres pairs non divisibles par 5
values = [x * 2 for x in range(50) if (x * 2) % 5 != 0]
print(values)

# Liste de mots
words = ["matin", "le", "pour", "lapin", "carotte", "justesse", "ambroisie", "cuticule", "aube", "flanc", "flan"]
# Créer une liste avec uniquement les mots de plus de 4 lettres
short_words = [w for w in words if len(w) > 4]
print(short_words)
