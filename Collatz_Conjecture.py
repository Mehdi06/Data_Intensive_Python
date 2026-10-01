def Collatz (valeur):
    if valeur % 2 == 0:
        return valeur/2
    else :
        return valeur*3+1

####################################

val = 1552
print(int(val))
while val!=1 : 
    
    val = Collatz(int(val))
    print(int(val))
    



