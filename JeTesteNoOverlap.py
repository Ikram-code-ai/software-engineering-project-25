# test_no_overlap.py

from bitpackingNoOverlap import BitPackingNoOverlap

# on crée un objet avec 8 bits par entier
packer = BitPackingNoOverlap(8)

tableau = [5, 10, 255, 12, 8, 7]
print("original :", tableau)

# compression
compressed = packer.compress(tableau)
print("compressé :", compressed)

# décompression
decompressed = packer.decompress()
print("décompressé :", decompressed)

# test d'accès direct
print("élément 2 :", packer.get(2))
