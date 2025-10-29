# src/bitpackingOverflow.py

from bitpacking_base import BitPacking

 # version avec overflow area certains nb trop grands sont stocké a part
class BitPackingOverflow(BitPacking):
    
    def __init__(self, k_bits, seuil):
        
        super().__init__(k_bits)    # k_bits = nombre de bits normal pour les petits nombres
        self.seuil = seuil        # seuil = valeur max qu on peut coder sans overflow
        self.overflow = []   # laa zone de depassement

    def compress(self, tableau):
        # check tous les entier du tableau
        compressed = []
        for val in tableau:
            if val > self.seuil:  # si valeur trop grande on met un marqueur
                index = len(self.overflow)
                self.overflow.append(val)
                compressed.append((1 << self.k_bits) | index)
            else:
                # valeur normale
                compressed.append(val)
        self.compressed_data = compressed
        return compressed

    def decompress(self):
        # on reconstruit le tableau en remplacant les val d'overflow
        decompressed = []
        for val in self.compressed_data:
            if val >> self.k_bits:  # si le bit de debordement est 1
                index = val & ((1 << self.k_bits) - 1)
                decompressed.append(self.overflow[index])
            else:
                decompressed.append(val)
        return decompressed
