# Mark Zuckerburg

> **CTF** : boroCTF 2026  
> **Catégorie** : `osint` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original

> Mark (from Meta) called me the other day and attached this photo. He told me he needed to remember what model camera he took his picture with. Could you help me?

### Traduction

> Mark (de Meta) m'a appelé l'autre jour et m'a envoyé cette photo. Il m'a dit qu'il avait besoin de se rappeler quel modèle d'appareil photo il avait utilisé pour prendre cette photo. Pourriez-vous m'aider ?

**Fichiers :**
- `Mark-Zuckerberg.png`

---
 
## Résolution
 
Pour trouver le flag nous devons aller chercher dans les données EXIF (ou meta data). 

### Solution Windows:

Aller dans les propriétés de l'image et dans le modèle nous pouvons trouver le modèle de caméra utilisée pour la photo qui est `boroCTF{M3+a_d@ta_1s_M7_Fa40rite}`

### Solution Linux : 

```bash
exiftool Mark-Zuckerberg.jpg | grep -i "Model"
```
 
---
 
## Flag
 
```
boroCTF{M3+a_d@ta_1s_M7_Fa40rite}
```
