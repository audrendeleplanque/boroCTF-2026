# Cracking the Vault

> **CTF** : boroCTF 2026  
> **Catégorie** : `web` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Solarity

---

## 📝 Description

### Texte originial

> Apparently this banking system is super secure and would never store the password somewhere in plain sight...

### Traduction

> Apparemment, ce système bancaire est ultra-sécurisé et ne stockerait jamais le mot de passe à la vue de tous...

**Accès** : `https://qphi2o7slkwc.boroctf.com/`

---
 
## Résolution
 
Il faut appuyer sur la touche `F12` pour entrer dans la console développeur. 

Dans la balise script, nous avons : 

```js
        
const correctPassword = "passworduwu";

document.getElementById("vaultForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const input = document.getElementById("passwordInput").value;
    const messageEl = document.getElementById("message");
    
    if (input === correctPassword) {
        messageEl.textContent = "✓ Correct! Flag: boroCTF{th3_p@th_l3ss_tr@vers3d}";
        messageEl.className = "success";
    } else {
        messageEl.textContent = "✗ Wrong password.";
        messageEl.className = "error";
    }
});
    
```
---
 
## Flag
 
```
boroCTF{th3_p@th_l3ss_tr@vers3d}
```