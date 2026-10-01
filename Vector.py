import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self._x = x
        #self.__y = y

    def changeVal(self, valX, valY):
        self.x = valX
        self.y = valY

    def norm(self):
        return math.sqrt(self.x**2+self.y**2)
    
##################################################

vecteur = Vector(9, 8)

print(vecteur.x)
print(vecteur.y)
print(vecteur.norm())
print(dir(vecteur))