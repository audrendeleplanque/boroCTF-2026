# Not the Flag

> **CTF** : boroCTF 2026  
> **Catégorie** : `crypto` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : ForeverFlames

---

## 📝 Description

### Texte original
> Challenge: So is this not the flag? If its not not, then what else?
> 9d 90 8d 90 bc ab b9 84 8b 97 ce db a0 96 8c a0 91 cf 8b a0 91 90 8b a0 8b 97 cc a0 99 93 bf 98 82

### Traduction
> Question : Ce n'est donc pas le drapeau ? Si ce n'est pas ça, alors qu'est-ce que c'est ?
> 9d 90 8d 90 bc ab b9 84 8b 97 ce db a0 96 8c a0 91 cf 8b a0 91 90 8b a0 8b 97 cc a0 99 93 bf 98 82

---
 
## Résolution
 
Cette suite de chiffre :

```
9d 90 8d 90 bc ab b9 84 8b 97 ce db a0 96 8c a0 91 cf 8b a0 91 90 8b a0 8b 97 cc a0 99 93 bf 98 82
```

Prenons le premier octet de votre séquence : `9d` :

`9d` en hexadécimal vaut 157 en décimal.
On applique l'inversion : **255 - 157 = 98.**
En regardant dans la table ASCII, le code **98** correspond à la lettre **b**.

En répétant cette opération (`FF - valeur hexadécimale`) pour chaque bloc, on traduit progressivement la séquence en texte lisible :

90 -> **o**

8d -> **r**

90 -> **o**

bc -> **C**

...et ainsi de suite.

---
 
## Flag
 
```
boroCTF{th1$_is_n0t_not_th3_fl@g}
```