# kitty kitty meow meow

> **CTF** : boroCTF 2026  
> **Catégorie** : `forensics` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte original

> *aww... so cute!*

### Traduction

> *Oh... Trop mignon !*

**Fichiers fournis** :
- `meow.jpg`

---
 
## Résolution
 
Une fois l'image téléchargée on doit taper cette commande : 

```bash
strings meow.jpg | grep "boro"
```

Voici la sortie de la commande : 

`boroCTF{f0r3nsic_@nalysis#}`

---
 
## Flag
 
```
boroCTF{f0r3nsic_@nalysis#}
```