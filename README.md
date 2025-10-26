# software engineering project 2025
# Ikram BENCHALAL 22015893 

j’ai commencé le projet avec la création du fichier **bitpacking_base.py**
c’est un premier fichier qui sert de base pour toute la suite du projet
dedans j’ai créé la classe `BitPacking`, qui va être la “mère” de toutes les autres versions de compression

j’y ai mis les fcts principales mais pas encore leur contenu complet, juste la structure pour bien organiser le code :

- `compress()` : va servir à compresser un tableau d’entiers  
- `decompress()` : fera l’inverse pour retrouver le tableau d’origine  
- `get(i)` : va nous permettre d’accéder directement à un élément precis du tableau compressé  
- `mesurer_temps()` : mesure combien de temps prend une fonction (utile pour les tests et les comparaisons de vitesse plus tard)

pour l’instant la classe ne fait encore rien de concret, mais elle prépare le terrain pour les versions à venir
j’ai aussi ajouté des petits commentaires simples pour que le code reste clair et facile à suivre  

j’ai choisi de travailler sur la méthode **no-overlap**, parce qu’elle est plus simple et logique 
c’est celle ou chaque entier reste dans un bloc de 32 bits, sans se couper entre deux blocs  
je vais continuer demain avec le fichier où je mettrai la vraie logique de compression celle du noOverlap
