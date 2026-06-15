# Fast reactions

> **CTF** : boroCTF 2026  
> **Catégorie** : `pwn` · **Points** : 100 · **Solves** : 42  
> **Difficulté** : easy  
> **Auteur** : Franklin

---

## 📝 Description

### Texte original

> Need higher WPM? Try monkeytype.

### Traduction

> Besoin de plus de mots par minutes ? Essaies monkeytype.

**Accès** : `nc tnkemaq46125.boroctf.com 56354`

---
 
## Résolution
 
Pour se connecter au challenge il faut taper la commande suivante dans un terminal :

```
nc tnkemaq46125.boroctf.com 56354
```

Le programme nous réponds ceci : 

```
Please enter <NOMBRE ALETOIRE EN HEX> characters!
```

Pour résoudre ce challenge nous devons l'automatiser parce que le temps de réaction est très court. Nous allons faire un programme python (`solve.py`):

```py
import socket
import re

# Configuration de la cible
HOST = 'tnkemaq46125.boroctf.com'
PORT = 56354

def main():
    # Création du socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"[*] Connexion à {HOST}:{PORT}...")
        s.connect((HOST, PORT))
        
        # Réception du message d'accueil
        # On lit un chunk de données (1024 octets max)
        data = s.recv(1024).decode('utf-8')
        print(f"[<] Reçu du serveur : {data.strip()}")
        
        # Recherche du pattern hexadécimal (ex: 0x193) via une regex
        match = re.search(r'(0x[0-9a-fA-F]+)', data)
        
        if match:
            hex_str = match.group(1)
            # Conversion de la chaîne hexadécimale en entier (base 16)
            dec_val = int(hex_str, 16)
            print(f"[*] Valeur extraite : {hex_str} -> {dec_val} en décimal")
            
            # Création de la charge utile (payload)
            # On génère une chaîne de 'A' de la longueur demandée
            payload = 'A' * dec_val
            print(f"[*] Envoi de {len(payload)} caractères...")
            
            # Envoi au serveur. 
            # Note : certains serveurs nécessitent un retour à la ligne b'\n' à la fin.
            # Si le script bloque, essaie : s.sendall(payload.encode() + b'\n')
            s.sendall(payload.encode('utf-8') + b'\n')
            
            # Réception de la réponse du serveur (probablement le flag !)
            response = s.recv(4096).decode('utf-8')
            print(f"[<] Réponse finale :\n{response}")
            
        else:
            print("[-] Impossible de trouver un nombre hexadécimal dans la réponse.")

if __name__ == '__main__':
    main()
```

Nous pouvons le lancer avec la commande : 

```bash
python3 solve.py
```

Voici la sortie : 

```text
[*] Connexion à tnkemaq46125.boroctf.com:56354...
[<] Reçu du serveur : Please enter 0x145 characters!
[*] Valeur extraite : 0x145 -> 325 en décimal
[*] Envoi de 325 caractères...
[<] Réponse finale :
Nice job! Flag: boroCTF{Hum@n1y_im7o5s!ble}
```

---
 
## Flag
 
```
boroCTF{Hum@n1y_im7o5s!ble}
```
