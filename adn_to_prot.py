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
code_genetique ={
    'S': 'Sérine',
    'F': 'Phénylalanine',
  'TTA':'L', # Leucine

  'TTG':'L', # Leucine

  'TAC':'Y', # Tyrosine

  'TAT':'Y', # Tyrosine

  'TAA':'*', # Codon Stop

  'TAG':'*', # Codon Stop

  'TGC':'C', # Cystéine

  'TGT':'C', # Cystéine

  'TGA':'*', # Codon Stop

  'TGG':'W', # Tryptophane

  'CTA':'L', # Leucine

  'CTC':'L', # Leucine

  'CTG':'L', # Leucine

  'CTT':'L', # Leucine

  'CCA':'P', # Proline

  'CCC':'P', # Proline

  'CCG':'P', # Proline

  'CCT':'P', # Proline

  'CAC':'H', # Histidine

  'CAT':'H', # Histidine

  'CAA':'Q', # Glutamine

  'CAG':'Q', # Glutamine

  'CGA':'R', # Arginine

  'CGC':'R', # Arginine

  'CGG':'R', # Arginine

  'CGT':'R', # Arginine

  'ATA':'I', # Isoleucine

  'ATC':'I', # Isoleucine

  'ATT':'I', # Isoleucine

  'ATG':'M', # Méthionine

  'ACA':'T', # Thréonine

  'ACC':'T', # Thréonine

  'ACG':'T', # Thréonine

  'ACT':'T', # Thréonine

  'AAC':'N', # Asparagine

  'AAT':'N', # Asparagine

  'AAA':'K', # Lysine

  'AAG':'K', # Lysine

  'AGC':'S', # Sérine

  'AGT':'S', # Sérine

  'AGA':'R', # Arginine

  'AGG':'R', # Arginine

  'GTA':'V', # Valine

  'GTC':'V', # Valine

  'GTG':'V', # Valine

  'GTT':'V', # Valine

  'GCA':'A', # Alanine

  'GCC':'A', # Alanine

  'GCG':'A', # Alanine

  'GCT':'A', # Alanine

  'GAC':'D', # Acide Aspartique

  'GAT':'D', # Acide Aspartique

  'GAA':'E', # Acide Glutamique

  'GAG':'E', # Acide Glutamique

  'GGA':'G', # Glycine

  'GGC':'G', # Glycine

  'GGG':'G', # Glycine

  'GGT':'G', # Glycine
  }


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

acide_amine = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"

def traduction(arn_m):
    codon = 'AAU'
    valeur_base = {'U': 0, 'C': 1, 'A': 2, 'G': 3}
    index = valeur_base[codon[0]] * 16 + valeur_base[codon[1]] * 4 + valeur_base[codon[2]]
    print(acide_amine[index])




traduction('coucou')