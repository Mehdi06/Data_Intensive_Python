import statistics

def lecture_fichier():
# Lecture de toutes les lignes dans une liste
    with open("downld02.txt", "r", encoding="utf-8") as f:
        lignes = f.readlines()
    return lignes

def transforme_to_value(lignes):
    valeurs_Par_Colonne = []
    for x in range(len(lignes)) :
        valeurs_Par_Colonne.append([None for y in range(30)])
        #for y in range(30):
        #    valeurs_Par_Colonne[x].append(None)
    i = 0
    for ligne in lignes[3:]:
        valeurs_Ligne = ligne.split()
        valeurs_Par_Colonne[i][0] = valeurs_Ligne[0]
        valeurs_Par_Colonne[i][1] = valeurs_Ligne[1]
        valeurs_Par_Colonne[i][2] = valeurs_Ligne[2]
        valeurs_Par_Colonne[i][3] = valeurs_Ligne[3]
        valeurs_Par_Colonne[i][4] = valeurs_Ligne[4]
        valeurs_Par_Colonne[i][5] = valeurs_Ligne[5]
        valeurs_Par_Colonne[i][6] = valeurs_Ligne[6]
        valeurs_Par_Colonne[i][7] = valeurs_Ligne[7]
        valeurs_Par_Colonne[i][8] = valeurs_Ligne[8]
        valeurs_Par_Colonne[i][9] = valeurs_Ligne[9]
        valeurs_Par_Colonne[i][10] = valeurs_Ligne[10]
        valeurs_Par_Colonne[i][11] = valeurs_Ligne[11]
        valeurs_Par_Colonne[i][12] = valeurs_Ligne[12]
        valeurs_Par_Colonne[i][13] = valeurs_Ligne[13]
        valeurs_Par_Colonne[i][14] = valeurs_Ligne[14]
        valeurs_Par_Colonne[i][15] = valeurs_Ligne[15]
        valeurs_Par_Colonne[i][16] = valeurs_Ligne[16]
        valeurs_Par_Colonne[i][17] = valeurs_Ligne[17]
        valeurs_Par_Colonne[i][18] = valeurs_Ligne[18]
        valeurs_Par_Colonne[i][19] = valeurs_Ligne[19]
        valeurs_Par_Colonne[i][20] = valeurs_Ligne[20]
        valeurs_Par_Colonne[i][21] = valeurs_Ligne[21]
        valeurs_Par_Colonne[i][22] = valeurs_Ligne[22]
        valeurs_Par_Colonne[i][23] = valeurs_Ligne[23]
        valeurs_Par_Colonne[i][24] = valeurs_Ligne[24]
        valeurs_Par_Colonne[i][25] = valeurs_Ligne[25]
        valeurs_Par_Colonne[i][26] = valeurs_Ligne[26]
        valeurs_Par_Colonne[i][27] = valeurs_Ligne[27]
        valeurs_Par_Colonne[i][28] = valeurs_Ligne[28]
        valeurs_Par_Colonne[i][29] = valeurs_Ligne[29]
        i += 1
    return valeurs_Par_Colonne

def renvoi_une_colonne(valeurs_Par_Colonne):
    valeurs_Colonne = []
    for x in range(len(valeurs_Par_Colonne[2])) :
        valeurs_Colonne.append(valeurs_Par_Colonne[x][2])
    return valeurs_Colonne

def calcule_et_affiche(valeurs_Temperature):
    temp_Max = max(valeurs_Temperature)
    temp_Min = min(valeurs_Temperature)
    #temp_ecart_type = statistics.stdev(valeurs_Temperature)
    print("Valeur max est de ", temp_Max)
    print("Valeur min est de ", temp_Min)
    #print("L'ecart type est de ", temp_ecart_type)

##################################################

if __name__ == "__main__":
    lecture_lignes = lecture_fichier()
    valeurs = transforme_to_value(lecture_lignes)
    colonne = renvoi_une_colonne(valeurs)
    print(colonne)
    #calcule_et_affiche(choix)
