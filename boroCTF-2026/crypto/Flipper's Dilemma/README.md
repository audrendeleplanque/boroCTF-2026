# Flipper's Dilemma

> **CTF** : boroCTF 2026  
> **Catégorie** : `crypto` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original
> Why do we flip a coin when we have to make a hard choice? Maybe the flipping here isn't so random. I flipped it once yet still 0x15 times.
```
wzgzVASnS4|eE${J%`>h
```

### Traduction
> Pourquoi tirons-nous à pile ou face quand nous devons faire un choix difficile ? Peut-être que ce tirage n'est pas si aléatoire que ça. Je l'ai tiré une fois, mais j'ai quand même obtenu 0x15 fois.

```
wzgzVASnS4|eE${J%`>h
```

---
 
## Résolution
 
En appliquant un XOR avec la valeur 21 sur l'ensemble de ta chaîne wzgzVASnS4|eE${J%>h`, on obtient le drapeau complet.

Il est possible d'exécuter le script `solve.py` suivant : 

```py
texte_chiffre = "wzgzVASnS4|eE${J%`>h"
cle = 21

texte_clair = "".join(chr(ord(c) ^ cle) for c in texte_chiffre)

print(texte_clair)
# Résultat : boroCTF{F!ipP1n_0u+}
```

---
 
## Flag
 
```
boroCTF{F!ipP1n_0u+}
```