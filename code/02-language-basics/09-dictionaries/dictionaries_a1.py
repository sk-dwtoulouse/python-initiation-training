# Conditions météo
meteo = {"Pau": (21.0, "Nuageux", 1015), "Gap": (20.3, "Dégagé", 1019), "Osny": (19.1, "Brouillard", 1015)}

# Conditions avec uniquement la température comme valeur associée
converted = {ville: meteo[ville][0] for ville in meteo}
print(converted)
