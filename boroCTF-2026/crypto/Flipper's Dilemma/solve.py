texte_chiffre = "wzgzVASnS4|eE${J%`>h"
cle = 21

texte_clair = "".join(chr(ord(c) ^ cle) for c in texte_chiffre)

print(texte_clair)
# Résultat : boroCTF{F!ipP1n_0u+}