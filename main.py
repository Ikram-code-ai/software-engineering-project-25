# src/main.py

from bitpacker_factory import BitPackerFactory

def afficher_resultats(mode, k_bits=8, seuil=None):
    print(f"\n--- test du mode {mode} ---")
    compresseur = BitPackerFactory.create(mode, k_bits, seuil)
    data = [5, 10, 255, 12, 8, 7, 1000, 4, 2]
    print("original :", data)

    compresse = compresseur.compress(data)
    print("compressé :", compresse)

    decompresse = compresseur.decompress()
    print("décompressé :", decompresse)

if __name__ == "__main__":
    afficher_resultats("no-overlap", 8)
    afficher_resultats("overlap", 8)
    afficher_resultats("overflow", 8, seuil=200)
