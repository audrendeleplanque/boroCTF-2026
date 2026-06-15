# Coming Together

> **CTF** : boroCTF 2026  
> **Catégorie** : `pwn` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original

> You have yours and I have mine. Together we have something larger than ourselves.

### Traduction

> Tu as le tien et j'ai le mien. Ensemble, nous formons quelque chose qui nous dépasse.

**Accès** : `nc oq7qaruz5vsw.boroctf.com 25287`

---
 
## Résolution
 
Si on décompose le programme avec un logiciel comme **Cutter**, nous avons ceci : 

```c
/* jsdec pseudo code output */

/* C:\Users\admin\Downloads\chal @ 0x11e9 */

#include <stdint.h>


int32_t main (void) {

uint32_t var_7ch;

int64_t var_78h;

unsigned long long var_74h;

FILE * stream;

char * str;

char * s;

int64_t canary;

rax = *(fs:0x28);

canary = *(fs:0x28);

eax = 0;

rax = "What number will you contribute?";

puts (rax);

rax = &str;

fgets (rax, 0xc, *(stdin));

var_78h = 2;

rax = &str;

rdi = rax;

eax = atoi ();

var_7ch = eax;

if (var_7ch > 0x2710) {

rax = "Wow there, try not to out do my number too much.";

puts (rax);

var_7ch = 1;

}

if (var_7ch < 0) {

rax = "No negatives!";

puts (rax);

var_7ch = -var_7ch;

}

edx = var_7ch;

eax = var_78h;

eax += edx;

var_74h = eax;

if (var_74h < 0) {

rax = "Huh? That's not supposed to happen.";

puts (rax);

rax = data_00002094;

rsi = rax;

rax = "flag.txt";

rax = fopen (rax, rsi);

stream = rax;

rdx = rax;

rax = &s;

fgets (rax, 0x40, rdx);

rax = &s;

puts (rax);

eax = 1;

} else {

eax = var_74h;

esi = var_74h;

rax = "Our total is %d! Good work everyone!\n";

eax = 0;

printf (rax);

eax = 0;

}

rdx = canary;

rdx -= *(fs:0x28);

if (rdx != 0) {

stack_chk_fail ();

}

return rax;

}
```

La condition qui nous intéresse est la suivante : 

```c
if (var_74h < 0)
```

Pour arriver à cette dernière nous devons utiliser **l'Integer Overflow**.
Pour faire ceci nous devons entrer `-2147483648` quand le programme nous demande un nombre. Ce qui va nous donner ce résultat : 

```text
What number will you contribute?
-2147483648
No negatives!
Huh? That's not supposed to happen.
boroCTF{tw0s_c0mpl3men+_M3}
```

---
 
## Flag
 
```
boroCTF{tw0s_c0mpl3men+_M3}
```
