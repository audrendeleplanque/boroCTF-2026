# Disco

> **CTF** : boroCTF 2026  
> **Catégorie** : `crypto` · **Points** : 200 · **Solves** : 42  
> **Difficulté** : medium  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original
> The hexagonal colors are simply beautiful.

### Traduction
> Les couleurs hexagonales sont tout simplement magnifiques.

**Fichiers fournis** :
- `dance.png`
---
## Résolution

Si on examine les valeurs RGB de chaque carrés : 

| # | RGB |
|---:|:---|
| 1 | rgb(98, 111, 114) |
| 2 | rgb(111, 67, 84) |
| 3 | rgb(70, 123, 110) |
| 4 | rgb(69, 118, 51) |
| 5 | rgb(114, 95, 108) |
| 6 | rgb(48, 36, 101) |
| 7 | rgb(95, 89, 111) |
| 8 | rgb(85, 52, 95) |
| 9 | rgb(66, 101, 64) |
| 10 | rgb(116, 125, 0) |
| 11 | rgb(0, 0, 0) |
| 12 | rgb(0, 0, 0) |

Si nous prenons chaque valeur de `rouge`, `vert` et `bleu`, nous obtenons :

```text
98 111 114 111 67 84 70 123 110 69 118 51 114 95 108 48 36 101 95 89 111 85 52 95 66 101 64 116 125 0 0 0 0 0 0 0
```

Décodé en ASCII cela donne : 

```text
boroCTF{nEv3r_l0$e_YoU4_Be@t}
```

---
## Flag


```text
boroCTF{nEv3r_l0$e_YoU4_Be@t}
```