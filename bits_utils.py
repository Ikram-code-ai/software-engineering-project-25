# src/bit_utils.py
#c juste un petit module a utiliser apres avec des fonctions utiles pour manipuler les bits

# pour retourner le nb de bits necessaires pour representer une valeur
def bits_necessaires(valeur):
    
    if valeur == 0:
        return 1
    return valeur.bit_length()

# pour retourner un masque binaire sur k bits 
def masque(k):
    # retourne un masque binaire sur k bits 
    return (1 << k) - 1

 #celle la retourne vrai si la valeur peut pas etre representée sur k bits
def depasse(valeur, k_bits):
    return valeur >= (1 << k_bits)
