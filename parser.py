import statistics


# Lecture de toutes les lignes dans une liste
with open("downld02.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()


valeurs_Temperature = []

for ligne in lignes[3:]:
    valeurs_Ligne = ligne.split()
    temperature_ext = valeurs_Ligne[2]
    valeurs_Temperature.append(float(temperature_ext)) 
    
#print(valeurs_Temperature)    
temp_Max = max(valeurs_Temperature)
temp_Min = min(valeurs_Temperature)
temp_ecart_type = statistics.stdev(valeurs_Temperature)

print("Valeur max est de ", temp_Max)
print("Valeur min est de ", temp_Min)
print("L'ecart type est de ", temp_ecart_type)
    
   
