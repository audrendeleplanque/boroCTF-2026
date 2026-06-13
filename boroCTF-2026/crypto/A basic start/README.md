# A basic start

> **CTF** : boroCTF 2026  
> **Catégorie** : `crypto` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original
> *We, the Boro Cyber Division have been spying on the chats of a group of local hackers. We used to be able to decrypt their chats from base64 but they seemed to have changed their encoding. Can you find out what they’re talking about now?*

### Traduction
> *Nous, la division cyber de Boro, avons espionné les discussions d'un groupe de hackers locaux. Auparavant, nous parvenions à décrypter leurs messages codés en base64, mais il semblerait qu'ils aient changé de codage. Pouvez-vous découvrir de quoi ils parlent maintenant ?*

**Fichiers fournis** :
- `chal.txt`

---
 
## Résolution
 
On peut directement remarquer du base64 sur la première ligne :

```
VXNlcjE6IEhleSwgSSB0aGluayB0aGUgQm9ybyB0ZWFtIGlzIG9udG8gdXMhClVzZXIyOiBObyBXYXkhIFRoZXkncmUgZ29pbmcgdG8gc2VuZCB0aGUgQ1RGIHBhcnRpY2lwYW50cyBhZnRlciB1cyEKVXNlcjM6IEl0J2xsIGJlIG9rYXksIHdlJ2xsIG1vdmUgdG8gYW5vdGhlciBiYXNlIGVuY29kaW5nIQ==
```

Une fois dans un décodeur on a : 

```
User1: Hey, I think the Boro team is onto us!
User2: No Way! They're going to send the CTF participants after us!
User3: It'll be okay, we'll move to another base encoding!
```

En se penchant sur la deuxième ligne on peut voir que c'est du base91 : 

```
j2_1+iZB_6AveF[p/Uxg,WT[#F]4pE&m:%gZ6=0{8!Z%F.0Dj2_1rjZB!8O;R@RnqM_1:WGk$yV%J_;mz2gZY^rN$F90axFl]UgZk>;N%y60;mYiSP8=SH)S<Ry*yCrbVu_15Wy{L%;EU,fr&A2N|ir}XxI(pBZ%w<d9P
```
Une fois dans un décodeur on a :

```
User1: Okay we're on the new encoding.
User2: You wonder if anyones ever reading your messages?
User1: Nope. boroCTF{B@5ics_0f_B@si6s}
```

---
 
## Flag
 
```
boroCTF{B@5ics_0f_B@si6s}
```