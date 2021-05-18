# A - adénine | C - cytosine | G - guanine | T - thymine | U - uracile
BASES = {'A', 'T', 'C', 'G', 'U'}

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

# Nous allons partir sur un brin de 64, attention, pas de U dans l'ADN !!
adn = []

def arn_m(adn, initial, final):
    """
        Prélève une séquence de l'ADN de initial à final et retourne un ARN messagé
        T  -> A
        A  -> U
        C <-> G
    """
    pass