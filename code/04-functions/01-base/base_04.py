"""Fonction qui calcule un quotient."""


def quotient(numerator, denominator=1):
    """
    Fonction de quotient.

    Renvoie `None` si l'argument `denominator` vaut 0.

    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        # Si impossible d'évaluer l'expression ligne 4
        return None


# Tester plusieurs arguments pour la fonction
print(quotient(10, denominator=4))
print(quotient(10, denominator=-1))
print(quotient(1, denominator=0))
print(quotient(5))
