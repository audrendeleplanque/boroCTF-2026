# Grep'n it

> **CTF** : boroCTF 2026  
> **Catégorie** : `forensics` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original

> I lost my flag in a stockpile of fake flags :(. Can you help me find it?

### Traduction

> J'ai perdu mon drapeau dans une pile de faux drapeaux :(. Tu peux m'aider à le retrouver ?

**Fichiers fournis** :
- `chal`

---
 
## Résolution

Il faut tapper la commande suivante : 

```bash
cat chal| grep "boro"
```

Voici la sortie de la commande : 

```text
boroCTF{G63p_G0d}
```

---
 
## Flag
 
```
boroCTF{G63p_G0d}
```