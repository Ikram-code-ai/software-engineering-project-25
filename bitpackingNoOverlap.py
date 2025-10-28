# src/bitpacking_no_overlap.py

from bitpacking_base import BitPacking

class BitPackingNoOverlap(BitPacking):

    # version sans chevauchement (no-overlap)
    # ici chaque entier compressé reste dans un bloc de 32 bits maximum
    
    def __init__(self, k_bits):
        # on appelle le constructeur de la classe de base
        super().__init__(k_bits)

    def compress(self, tableau):
        # cette fonction compresse un tableau d'entiers
        # chaque entier est représenté sur k bits sans dépasser 32 bits

        compressed = []
        current = 0          # nombre 32 bits en cours de remplissage
        bits_utilises = 0    # combien de bits sont déjà utilisés dans le bloc

        for val in tableau:
            # si l'entier ne rentre pas dans le bloc courant, on passe au suivant
            if bits_utilises + self.k_bits > 32:
                compressed.append(current)
                current = 0
                bits_utilises = 0

            # on place la valeur au bon endroit avec un décalage de bits
            current |= (val & ((1 << self.k_bits) - 1)) << bits_utilises
            bits_utilises += self.k_bits

        # s'il reste un bloc partiellement rempli, on l'ajoute aussi
        if bits_utilises > 0:
            compressed.append(current)

        self.compressed_data = compressed
        return compressed

    def decompress(self):
        # cette fonction décompresse le tableau compressé
        # elle fait l'opération inverse : on relit les entiers de k bits un par un

        decompressed = []
        for bloc in self.compressed_data:
            bits_lus = 0
            while bits_lus + self.k_bits <= 32:
                val = (bloc >> bits_lus) & ((1 << self.k_bits) - 1)
                decompressed.append(val)
                bits_lus += self.k_bits
        return decompressed

    def get(self, i):
        # retourne la valeur du i-ème entier dans le tableau original
        # on retrouve dans quel bloc et à quel décalage il se trouve

        bloc_index = (i * self.k_bits) // 32
        bit_offset = (i * self.k_bits) % 32
        bloc = self.compressed_data[bloc_index]
        val = (bloc >> bit_offset) & ((1 << self.k_bits) - 1)
        return val
