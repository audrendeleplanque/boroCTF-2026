# Beyond the Homepage

> **CTF** : boroCTF 2026  
> **Catégorie** : `web` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte originial

> There's more to what you see...

### Traduction

> Ce n'est pas tout...

**Accès** : `https://6ox3t3alzl51.boroctf.com/`

---
 
## Résolution
 
En appuyant sur `Crtl + U` on peut voir le code source de la page. 

```HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>boroCTF / Beyond the Webpage</title>
    <!--boroCTF{d3v3l0peR_t001s}-->
</head>

<body>
    <h1>boroCTF</h1>
    <p>Sometimes there's more to what you can see.<br><br>(Hint: You might want to use a tool that a developer might use)</p>
</body>
</html>

```
 
---
 
## Flag
 
```
boroCTF{d3v3l0peR_t001s}
```