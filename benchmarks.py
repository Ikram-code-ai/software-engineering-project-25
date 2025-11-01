# src/benchmarks.py

import time
from bitpackingNoOverlap import BitPackingNoOverlap
from bitpackingOverlap import BitPackingOverlap
from bitpackingOverflow import BitPackingOverflow

def tester_performance():
    # on crée un tableau de 10 000 entiers entre 0 et 299
    data = [i % 300 for i in range(10000)]
    taille = len(data)  # nb d'éléments à traiter

    print("=== test de performance des 3 méthodes ===")

    # test no-overlap
    start = time.time()
    BitPackingNoOverlap(8).compress(data)
    t_no = time.time() - start
    bw_no = taille / (t_no + 1e-9)  # calcul de la bandwidth (éléments/s)
    print(f"no overlap : {round(t_no, 6)} s  |  bandwidth = {round(bw_no, 2)} éléments/s")

    # test overlap
    start = time.time()
    BitPackingOverlap(8).compress(data)
    t_ov = time.time() - start
    bw_ov = taille / (t_ov + 1e-9)
    print(f"overlap : {round(t_ov, 6)} s  |  bandwidth = {round(bw_ov, 2)} éléments/s")

    # test overflow
    start = time.time()
    BitPackingOverflow(8, seuil=200).compress(data)
    t_of = time.time() - start
    bw_of = taille / (t_of + 1e-9)
    print(f"overflow : {round(t_of, 6)} s  |  bandwidth = {round(bw_of, 2)} éléments/s")

    # comparaison rapide
    print("\ncomparaison rapide :")
    print(f"- overlap vs no-overlap : {round(t_no - t_ov, 6)} s de différence")
    print(f"- overflow vs no-overlap : {round(t_no - t_of, 6)} s de différence")

if __name__ == "__main__":
    tester_performance()
