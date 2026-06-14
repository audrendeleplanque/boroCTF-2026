texte_chiffre = "?AEAGJ8NJF,\\0[d5JcE-"
cible = "boroCTF{h4EMr0n_0u+}"

# 1. Extraire la séquence XOR pour les 8 premiers caractères
cles_xor = [ord(c) ^ ord(p) for c, p in zip(texte_chiffre[:8], cible)]
print(f"Séquence de clés XOR trouvée : {cles_xor}")
# Résultat : [93, 46, 55, 46, 4, 30, 22, 53]

# 2. Tentative de déchiffrement en supposant que la clé se répète
texte_clair = ""
for i in range(len(texte_chiffre)):
    # Note : Si \0 est un octet nul unique (\x00), la longueur change et décale la clé
    texte_clair += chr(ord(texte_chiffre[i]) ^ cles_xor[i % len(cles_xor)])

print(f"Tentative de déchiffrement : {texte_clair}")