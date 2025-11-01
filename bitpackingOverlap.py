# src/bitpackingOverlap.py

from bitpacking_base import BitPacking

class BitPackingOverlap(BitPacking):
    # c version avec chevauchement des bits qui permet de mieux remplir les bloc de 32 bits
    
    def __init__(self, k_bits):
        super().__init__(k_bits)

    def compress(self, tableau):
        # on compresse les entier en les collant les uns apres les autres dans un flux de bits
        flux_bits = 0
        nb_bits_total = 0
        compresse = []

        for val in tableau:
            # on ajoute la valeur dans le flux
            flux_bits = (flux_bits << self.k_bits) | val
            nb_bits_total += self.k_bits

            # des qu on a un bloc complet de 32 bits on le stock
            while nb_bits_total >= 32:
                bloc = flux_bits >> (nb_bits_total - 32)
                compresse.append(bloc)
                flux_bits = flux_bits & ((1 << (nb_bits_total - 32)) - 1)
                nb_bits_total -= 32

        # si des bits restent a la fin on complete le dernier bloc
        if nb_bits_total > 0:
            compresse.append(flux_bits << (32 - nb_bits_total))

        self.compressed_data = compresse
        return compresse

    def decompress(self):
        # on decompresse les blocs pour retrouver le tableau initial
        resultat = []
        tampon = 0
        bits_restants = 0

        for bloc in self.compressed_data:
            tampon = (tampon << 32) | bloc
            bits_restants += 32

            while bits_restants >= self.k_bits:
                val = (tampon >> (bits_restants - self.k_bits)) & ((1 << self.k_bits) - 1)
                resultat.append(val)
                bits_restants -= self.k_bits

        return resultat