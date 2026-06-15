# Not Your Time

> **CTF** : boroCTF 2026  
> **Catégorie** : `rev` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original

> One of the trifecta of bitwise operations.

### Traduction

> L'une des trois opérations binaires fondamentales.

**Fichiers fournis** :
- `chal`

---
 
## Résolution
 
L'exécutable est un "crackme" classique. L'analyse du pseudo-code de la fonction `main` révèle la logique suivante :

Le programme stocke un tableau de `25 octets` en dur sur la pile.

Il lit l'entrée utilisateur via un `scanf`.

Il boucle sur les 25 caractères et compare chaque caractère saisi avec l'octet correspondant, après lui avoir appliqué un `Bitwise NOT (~)`.

Puisque la condition de validation est `input == ~target`, il suffit d'appliquer l'opération inverse (`0xFF - valeur`) sur les valeurs hardcodées pour retrouver le flag en clair.

Script de résolution (solve.py) :

```py
target = [
    0x9d, 0x90, 0x8d, 0x90, 0xbc, 0xab, 0xb9, 0x84, 
    0xb1, 0xcf, 0x8b, 0xa0, 0x91, 0xb0, 0xd4, 0xa0, 
    0x8b, 0xb7, 0xcc, 0xa0, 0xb9, 0xb3, 0xbf, 0x98, 0x82
]

flag = "".join(chr(0xFF - b) for b in target)
print(flag)
```

---
 
## Flag
 
```
boroCTF{N0t_nO+_tH3_FL@g}
```
