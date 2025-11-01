# Software Engineering Project 2025  
## Bit Packing – Data Compressing for Speed Up Transmission  
**Ikram BENCHALAL – 22015893**

---

## Environnement

- **Langage utilisé :** Python 3  
- **Éditeur recommandé :** Visual Studio Code  
- **Bibliothèques externes :** aucune (tout est en Python standard)  
- **Compilation :** non nécessaire (Python est interprété)

Pour exécuter le code, ouvrir un terminal dans le dossier du projet et utiliser :  
```bash
python nom_du_fichier.py 

Donc:

python main.py
python benchmarks.py


## Contenu du projet

| Fichier                  | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| `bitpacking_base.py`     | classe de base `BitPacking`, structure commune à toutes les versions |
| `bitpackingNoOverlap.py` | implémentation du mode **no-overlap**                                |
| `bitpackingOverlap.py`   | implémentation du mode **overlap**                                   |
| `bitpackingOverflow.py`  | implémentation du mode **overflow** (valeurs stockées à part)        |
| `bitpacker_factory.py`   | création automatique d’un packer selon le mode choisi                |
| `compression_mode.py`    | configuration des paramètres de compression                          |
| `bits_utils.py`          | fonctions utilitaires pour la manipulation des bits                  |
| `benchmarks.py`          | comparaison de performance et calcul de la bande passante            |
| `main.py`                | exécution globale et tests des trois modes                           |
| `JeTesteNoOverlap.py`    | test unitaire rapide du mode no-overlap                              |
| `README.md`              | notice d’utilisation (ce fichier)                                    |

## Utilisation

- **Exécuter** `main.py` pour lancer un test complet des trois modes.  
- **Exécuter** `benchmarks.py` pour mesurer la vitesse et la bande passante.  
- Les résultats de compression et de décompression s’affichent directement dans le terminal.

---

## Remarques

- Le code ne demande **aucune saisie utilisateur** (tout est automatisé).  
- Les tests sont exécutés directement depuis le fichier `main.py`.  
- Les résultats sont affichés dans la console sous forme de tableaux simples.

---

## Rapport

Le rapport du projet (explications, résultats et interprétations) sera ajouté ultérieurement sous le nom :  
**`rapport_BENCHALAL_IKRAM.pdf`**
