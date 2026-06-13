# File Me to the Moon

> **CTF** : boroCTF 2026  
> **Catégorie** : `forensics` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte original

> Frank sinatra accidentally deleted the file extension on one of his files!!!
> What file extension is it supposed to be???
> boroCTF{file_extension}

### Traduction

> Frank sinatra a supprimé l'extension de l'un de ses fichier accidentellement

**Fichiers fournis** :
- `superfile`

---
 
## Résolution
 
Une fois l'image téléchargée on doit taper cette commande : 

```bash
file superfile
```

Voici la sortie de la commande : 

`superfile: Microsoft PowerPoint 2007+`

On sait que les extensions de Microsoft PowerPoint 2007+ c'est `.pptx`

---
 
## Flag
 
```
boroCTF{pptx}
```