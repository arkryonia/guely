1-L'utilisateur soumet ses paramètres de connxion

2- L'application en avant-plan envoie ces paramètre sur le tokenURL de l'API

3- L'API vérifie les paramètre et répond avec un token
    - un token est juste une chaîne qui permet d'authentifier ce utilisateur.
        - Normalement, un token est défini pour s'expirer après quelques moments
        - Ainsi, si jamais le token devient vulnérable, le risque est moindre. 
4- L'application d'avant-plan enregistre temporairement ce token

5- L'utilisateur clique en avant-plan pour aller à une autre section

6- L'avant-plan a besoin d'obtenir plus de données de l'API:

    - Mais il a besoin de s'authentifier pour cette cible spécifique

    - Ainsi, pour s'authentifier avec l'API, il envoie l'entête Authorization avec la valeur du Bearer plus le token

    - Si le token cotient foobar, le contenu de l'entête de l'Authorization devrait être Bearer foobar