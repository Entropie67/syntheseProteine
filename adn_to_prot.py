# Alanine
# Arginine
# Asparagine
# Aspartate ou acide aspartique
# Cystéine
# Glutamate ou acide glutamique
# Glutamine
# Glycine
# Histidine
# Isoleucine
# Leucine
# Lysine
# Méthionine
# Phénylalanine
# Proline
# Pyrrolysine
# Sélénocystéine
# Sérine
# Thréonine
# Tryptophane
# Tyrosine
# Valine
# Nous allons utiliser le "tableau inverse" dans l'article de Wikipédia sur le code génétique
ACIDES_AMINES = {}

# A - adénine | C - cytosine | G - guanine | T - thymine | U - uracile
BASES = ('A', 'T', 'C', 'G', 'U')
COMPLEMENT = ('T', 'A', 'G', 'C')
# Un dictionnaire nous donnant la correspondance des bases
COMPLEMENT_DICO = dict(zip(BASES, COMPLEMENT))
print(COMPLEMENT_DICO)
# Nous allons partir sur un brin de 64, attention, pas de U dans l'ADN !!
#
from random import choice
adn = [choice(BASES[:-1]) for _ in range(16)]
print(f"Notre brin ADN : \n{adn}")


def arn_m(adn, initial, final):
    """
        Prélève une séquence de l'ADN de initial à final et retourne un ARN messagé
        T  -> A
        A  -> U
        C <-> G
    """
    sequence = adn[initial + 1: final + 2]
    print(sequence)
    arn_m = [COMPLEMENT_DICO[b] if b != "A" else "U" for b in sequence]
    return arn_m

print(f"L'arn messagé est :\n{arn_m(adn, 2, 13)}")


def traduction(arn_m):
    pass