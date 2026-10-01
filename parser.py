# Lecture de toutes les lignes dans une liste
with open("downld02.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()

# Optionnel : enlever les retours à la ligne (\n) de chaque fin de ligne
lignes_propres = [ligne.strip() for ligne in lignes]


#for i in range(len(lignes_propres)):
uneLigne = lignes_propres[3].split()
maxLigne = uneLigne[2]
print(maxLigne)
    
uneLigne = lignes_propres[4].split()
maxLigne = uneLigne[2]
print(maxLigne)

print(len(lignes_propres))
print(lignes_propres[3].split())
