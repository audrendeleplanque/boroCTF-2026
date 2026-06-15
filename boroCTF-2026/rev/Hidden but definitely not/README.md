# Hidden but definitely not

> **CTF** : boroCTF 2026  
> **Catégorie** : `rev` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original

> The most trite challenge concept.

### Traduction

> Le concept de défi le plus éculé qui soit.

**Fichiers fournis** :
- `password_protected`

---
 
## Résolution
 
Le programme ne stocke pas le mot de passe en clair au même endroit, il le "construit" en mémoire pour tromper les analyses trop simples.

Il commence par mettre la chaîne `"Rate5Stars"` dans la variable `s2` (via les valeurs hexadécimales `0x6174533565746152` et `0x7372` qui, lues à l'envers à cause du système Little Endian, forment ces mots).

Plus loin dans le code, il calcule la taille de ce début de mot de passe (`strlen()`) et vient y coller la suite en utilisant d'autres blocs hexadécimales : `0x4765737561636542` ("BecauseG"), `0x6c61684374616572` ("reatChal") et `0x65676e656c6c61` ("lenge").

Le mot de passe final est donc : `Rate5StarsBecauseGreatChallenge`

Si on exécuter le programme avec la commande suivante : 

```bash
./password_protected
```

La sortie : 

```
Give me the password (youll never find it it's just tooooo hard)
>
```

Et qu'on entre le mot de passe `Rate5StarsBecauseGreatChallenge`, nous avons : 

```
Give me the password (youll never find it it's just tooooo hard)
> Rate5StarsBecauseGreatChallenge
wow you really got me this time. if only i used better obfuscation techniques.
boroCTF{I_H8_M@7ing_StR1ng5_cHals}
```

---
 
## Flag
 
```
boroCTF{I_H8_M@7ing_StR1ng5_cHals}
```
