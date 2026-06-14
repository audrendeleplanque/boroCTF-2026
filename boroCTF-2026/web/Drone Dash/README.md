# Drone Dash

> **CTF** : boroCTF 2026  
> **Catégorie** : `web` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte originial

> Welcome to the neon grid, pilot. Your objective is simple: Land the drone on the pad in under 1.5 seconds.

### Traduction

> Bienvenue dans la grille néon, pilote. Ton objectif est simple : faire atterrir le drone sur la plate-forme en moins de 1,5 seconde.

**Accès** : `https://697vj046dbi3.boroctf.com`

---
 
## Résolution
 
Il faut entrer ce texte dans l'encadré :

```json
{
  "physics": {
    "Kp": 0.1,
    "Kd": 0.5,
    "Ki": 0.01
  }
}
```

Appuyer sur le bouton `Initiate flight` et après une petite attente le flag apparait.
 
---
 
## Flag
 
```
boroCTF{pr0totyp3_p0llut10n_dr0ne_d4sh}
```