# src/bitpacking_base.py

import time

class BitPacking:
    
    # classe de base pour compresser les entier (bit packing)
    # elle sert juste de structure commune pour les deux versions (overlap et no-overlap)
    
    def __init__(self, k_bits):
        
        self.k_bits = k_bits   # nb de bits utilisés pour representer chaque entier
        self.compressed_data = []

    def compress(self, tableau):
        # méthode à redéfinir dans les sous classes elle prend un tableau d'entiers et retourne une verqion compressée
        raise NotImplementedError("on va la revoir dans la sous classe")

    def decompress(self):
        # méthode à redéfinir dans les sous-classes elle va retourner la version decompressée du tableau org
        raise NotImplementedError("on va la revoir dans la sous classe")

    def get(self, i):
        # méthode à redéfinir elle retourne la valeur du i-ème entier dans le tableau org
        raise NotImplementedError("on va la revoir dans la sous classe")
   # pour mesurer le temps d'exécution d'une fct
    def mesurer_temps(self, fonction, *args):
        
        debut = time.perf_counter()
        resultat = fonction(*args)
        fin = time.perf_counter()
        duree = fin - debut
        return resultat, duree
