weight = 17_254_433  # Poids en grammes
tons = weight // 1_000_000  # Combien de paquets de 1 tonne
kilograms = (weight // 1_000) % 1_000  # Nombre de kilos restants sous la tonne
grams = weight % 1_000  # Nombre de grammes sous le kilo

# Afficher les unités
print("Tonnes :", tons)
print("Kilogrammes :", kilograms)
print("Grammes :", grams)
