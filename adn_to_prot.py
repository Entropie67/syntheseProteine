code_genetique ={
    'S': 'Sérine',
    'F': 'Phénylalanine',
    'L': 'Leucine',
    'Y': 'Tyrosine',
    '*': 'Codon Stop',
    'C': 'Cystéine',
    'W': 'Tryptophane',
    'P': 'Proline',
    'H': 'Histidine',
    'Q': 'Glutamine',
    'R': 'Arginine',
    'I': 'Isoleucine',
    'M': 'Méthionine',
    'T': 'Thréonine',
    'N': 'Asparagine',
    'K': 'Lysine',
    'V': 'Valine',
    'A': 'Alanine',
    'D': 'Acide Aspartique',
    'E': 'Acide Glutamique',
    'G': 'Glycine'
  }
# A - adénine | C - cytosine | G - guanine | T - thymine | U - uracile
BASES = ('A', 'T', 'C', 'G', 'U')
COMPLEMENT = ('T', 'A', 'G', 'C')
# Un dictionnaire nous donnant la correspondance des bases
COMPLEMENT_DICO = dict(zip(BASES, COMPLEMENT))

# Nous allons partir sur un brin de 64, attention, pas de U dans l'ADN !!
from random import choice, randint
adn = [choice(BASES[:-1]) for _ in range(16)]

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

acide_amine = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
def arn_to_codons(arn):
    nombre_de_codons = len(arn)//3
    liste_de_codons = []
    for i in range(nombre_de_codons):
        codon = []
        for j in range(3):
            codon.append(arn[i+j])
        liste_de_codons.append(codon)
    print(f"La liste des condons est : {liste_de_codons}")
    return liste_de_codons

def traduction(arn_m):
    proteine = []
    for codon in arn_m:
        valeur_base = {'U': 0, 'C': 1, 'A': 2, 'G': 3}
        index = valeur_base[codon[0]] * 16 + valeur_base[codon[1]] * 4 + valeur_base[codon[2]]
        print(acide_amine[index], "-->", code_genetique[acide_amine[index]])
        proteine.append(acide_amine[index])
    return proteine

def mutation(adn):
    """ Mutation par substitution"""
    taille_adn = len(adn)
    index = randint(0, taille_adn - 1)
    proba = randint(1, 750)
    copie_adn = adn[:]
    if proba == 5:
        copie_adn[index] = choice(BASES[:-1])
    return copie_adn

print(f"Notre brin ADN : \n{adn}")
print(f"L'arn messagé est :\n{arn_m(adn, 2, 13)}")
print(traduction(arn_to_codons(arn_m(adn, 2, 13))))

nombre_mutation = 0
nombre_replication = 10000000
for i in range(nombre_replication):
    if adn != mutation(adn):
        nombre_mutation += 1

print(f"{nombre_mutation} pour {nombre_replication}")