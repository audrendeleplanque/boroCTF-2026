# Physical Access >>

> **CTF** : boroCTF 2026  
> **Catégorie** : `osint` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte original

> Help!! I forgot my password and got locked out of my Windows PC!
> I need to get back in, what can I do?!
> What is one of the two files I can exploit in order to get back into my PC?
> Flag format: boroCTF{explorer.exe}

### Traduction

> Au secours !! J'ai oublié mon mot de passe et je ne peux plus accéder à mon PC Windows !
> Je dois récupérer l'accès, que puis-je faire ?!
> Quel est l'un des deux fichiers que je peux exploiter pour récupérer l'accès à mon PC ?
> Format du drapeau : boroCTF{explorer.exe}

---
 
## Résolution
 
Les deux fichiers historiques et principalement ciblés pour résoudre ce problème sont :

- `sethc.exe` : l'exécutable qui gère les touches rémanentes (Sticky Keys, activées en appuyant 5 fois sur Maj).

- `utilman.exe` : l'exécutable qui gère le gestionnaire d'utilitaires (Utility Manager, accessible via l'icône en bas à droite de l'écran de verrouillage).
 
---
 
## Flag
 
```
boroCTF{sethc.exe}
```
 
```
boroCTF{utilman.exe}
```