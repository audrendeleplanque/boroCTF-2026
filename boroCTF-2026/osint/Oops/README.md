# Oops...

> **CTF** : boroCTF 2026  
> **Catégorie** : `osint` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte original

> My friend (again) was telling me a story about how around two years ago, he may or may not have accidentally pushed a change to a file that disrupted millions of systems at an unprecedented scale.
> What was the general name of the configuration file that he modified that broke everything?
> Flag Format: boroCTF{file_name_67}

### Traduction

> Mon ami (encore lui) me racontait qu'il y a environ deux ans, il aurait peut-être accidentellement validé une modification sur un fichier qui aurait perturbé des millions de systèmes à une échelle sans précédent.
> Quel était le nom général du fichier de configuration qu'il a modifié et qui a tout fait planter ?
> Format du drapeau : boroCTF{file_name_67}

---
 
## Résolution
 
Ce challenge fait référence à la panne informatique mondiale massive provoquée par l'entreprise de cybersécurité **CrowdStrike** le 19 juillet 2024.

L'incident a été causé par une mise à jour automatique défectueuse d'un fichier de configuration lié à leur capteur Falcon. Cette petite modification a provoqué une erreur logique au niveau du noyau (kernel) de Windows, entraînant des écrans bleus de la mort (BSOD) et des boucles de redémarrage sur environ 8,5 millions de systèmes à travers le monde.

Le nom général de ce fichier de configuration spécifique est le **Channel File 291**
 
---
 
## Flag
 
```
boroCTF{channel_file_291}
```
