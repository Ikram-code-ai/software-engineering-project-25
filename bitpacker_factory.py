# src/bitpacker_factory.py

from bitpackingNoOverlap import BitPackingNoOverlap
from bitpackingOverlap import BitPackingOverlap
from bitpackingOverflow import BitPackingOverflow

class BitPackerFactory:
    # pour creer la bonne version compresseur selon le mode choidi

    @staticmethod
    def create(mode, k_bits=8, seuil=None):
        if mode == "no-overlap":
            return BitPackingNoOverlap(k_bits)
        elif mode == "overlap":
            return BitPackingOverlap(k_bits)
        elif mode == "overflow":
            if seuil is None:
                seuil = (1 << k_bits) - 1
            return BitPackingOverflow(k_bits, seuil)
        else:
            raise ValueError("mode inconnu (choisis entre 'no-overlap', 'overlap' ou 'overflow')")
