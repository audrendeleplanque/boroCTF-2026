# boro-senpai 1

> **CTF** : boroCTF 2026  
> **Catégorie** : `web` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte originial

> Muhahaha! The Organization thinks they can silence me, but I, Hououin Kyouma, have uncovered a lead. My assistant — the self-proclaimed neuroscience prodigy — harbors a secret so embarrassing it could shake the very fabric of her dignity. An old @channel handle. Find it, and her profile is yours. El. Psy. Kongroo.

### Traduction

> Muhahaha ! L'Organisation croit pouvoir me réduire au silence, mais moi, Hououin Kyouma, j'ai découvert une piste. Mon assistante — qui se proclame prodige des neurosciences — cache un secret si embarrassant qu'il pourrait ébranler les fondements mêmes de sa dignité. Un ancien pseudo sur @channel. Trouve-le, et son profil t'appartient. El. Psy. Kongroo.

**Accès** : `https://w03xj6cjsucj.boroctf.com`

---
 
## Résolution
 
On peut voir que dans la discussion dans le thread `Does time travel violate conservation of energy? Serious thread` que son "assistante" est connue sous le pseudo `KuriGohanandKamehameha`. 
En allant sur son profile avec l'URL : `https://w03xj6cjsucj.boroctf.com/profile/KuriGohanandKamehameha`, on peut voir le flag. 

Deuxième solution : 
Faire le gros bourin et tester tous les pseudo et tous les liens. Ca marche aussi...
 
---
 
## Flag
 
```
boroCTF{3l_psY_c0ngR00!}
```