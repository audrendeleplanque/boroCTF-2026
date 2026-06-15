# Boro Coin 2

> **CTF** : boroCTF 2026  
> **Catégorie** : `crypto` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original
> Congratulations! You got their private key! Little problem ... we have no clue what to do with it. Could you generate a signature for us :). Please have the recipiant be "Boro_Confiscation_Committee". Since you're emptying the wallet anyway, just reuse the nonse again.
> Note: This challenge does not contain a flag. You will need to submit the transaction signature (lowercase hex, no prefix) as the flag. Example: boroCTF{3045022100ed...}

### Traduction
> Félicitations ! Vous avez mis la main sur leur clé privée ! Petit problème… on ne sait pas trop quoi en faire. Pourriez-vous générer une signature pour nous :) ? Veuillez indiquer comme destinataire « Boro_Confiscation_Committee ». Puisque vous videz le portefeuille de toute façon, réutilisez simplement le nonce.
> Remarque : ce défi ne contient pas de drapeau. Vous devrez soumettre la signature de la transaction (hexadécimal en minuscules, sans préfixe) comme drapeau. Exemple : boroCTF{3045022100ed...}

---
 
## Résolution

### Calcul du solde restant

Avant de créer la transaction, il faut déterminer combien de "Boro Coins" contient encore le portefeuille. Le solde initial, avant toute transaction, était de 51.42 bc.
En itérant sur le fichier JSON, on additionne les fonds entrants et on soustrait les fonds sortants. (Note : on ignore la transaction 13 envoyée par le "Suspect" au "Suspect", qui s'annule elle-même).

- **Solde initial** : +51.42
- **Total des entrées (Incoming)** : +2300.21
- **Total des sorties (Outgoing)** : -2319.28
- **Solde final disponible** : 32.35 bc

Le message de notre nouvelle transaction à signer est donc :
`"Suspect:Boro_Confiscation_Committee:32.35"`

### Mathématiques pour forger la signature

Puisque nous réutilisons le nonce $k$, la composante $r$ de notre nouvelle signature sera identique à celle de notre collision initiale.

$$r = \text{0x2cbda85fc21f5e62f94d8378d2dad1a05bc5d5522d5a717f2bdf1df13d558ec7}$$

Il ne nous reste qu'à calculer la nouvelle composante $s$ en utilisant la clé privée $d$ que nous avons déduite à la partie 1 et le hash ($z$) de notre nouveau message :

$$s = k^{-1} (z_{nouveau} + d \cdot r) \pmod n$$

### Script d'exploitation (Suite)

Voici la suite du code pour construire cette signature et l'encoder correctement au format standard DER :

```py
# (Suite du script précédent...)

# Paramètres de la nouvelle transaction
amount_str = "32.35"
new_msg = f"Suspect:Boro_Confiscation_Committee:{amount_str}".encode()
z_new = int(hashlib.sha256(new_msg).hexdigest(), 16)

# Calcul du nouveau 's' avec le 'k', 'd' et 'r' existants
s_new = (pow(k, -1, n) * (z_new + d * r)) % n

# Convention ECDSA : s doit généralement être inférieur à n/2
if s_new > n // 2:
    s_new = n - s_new

def encode_der(r_val, s_val):
    """Encode les valeurs r et s en une chaîne hexadécimale formatée DER."""
    def int_to_bytes(val):
        hex_val = hex(val)[2:]
        if len(hex_val) % 2 != 0:
            hex_val = '0' + hex_val
        b = bytes.fromhex(hex_val)
        # Ajout d'un byte nul si le bit de poids fort est à 1 (pour forcer un entier positif en DER)
        if b[0] & 0x80:
            b = b'\x00' + b
        return b
    
    r_bytes = int_to_bytes(r_val)
    s_bytes = int_to_bytes(s_val)
    
    # Structure DER : 0x30 [longueur totale] 0x02 [longueur r] [r] 0x02 [longueur s] [s]
    der = bytes([0x02, len(r_bytes)]) + r_bytes + bytes([0x02, len(s_bytes)]) + s_bytes
    der = bytes([0x30, len(der)]) + der
    return der.hex()

print(f"Signature forgée (DER) : {encode_der(r, s_new)}")
```

---
 
## Flag
 
```
boroCTF{304402202cbda85fc21f5e62f94d8378d2dad1a05bc5d5522d5a717f2bdf1df13d558ec70220033a47e398c6d81b053a235884c13b41f5618a6fa85715198a09beefdd5c3342}
```