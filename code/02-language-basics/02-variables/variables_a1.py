distance = 42195  # distance en mètres
kilometers = distance // 1000  # nombre entier de paquets de 1 000
meters = distance % 1000  # Reste après division entière par 1 000

# Affichage avec un peu de texte en plus.
print(kilometers, "km et", meters, "mètres.")

