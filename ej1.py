
import math


class Punto:

    def __init__(self,valor_x = 0, valor_y = 0):
        self.valor_x = valor_x
        self.valor_y = valor_y

    def punto(self):
        return (self.valor_x,self.valor_x)

    def cuadrante(self):
        if self.valor_x==0 and self.valor_y!=0:
            return "Esta situado sobr el eje Y"
        
        elif self.valor_x!=0 and self.valor_y==0:
            return "Esta situado sobre el eje X"

        elif self.valor_x==0 and self.valor_y==0:
            return "Esta situado sobre el ORIGEN"

        elif self.valor_x>0 and self.valor_y>0:
            return "Esta en el PRIMER cuadrante"

        elif self.valor_x<0 and self.valor_y>0:
            return "Esta en el SEGUNDO cuadrante"

        elif self.valor_x<0 and self.valor_y<0:
            return "Esta en el TERCER cuadrante"

        elif self.valor_x>0 and self.valor_y<0:
            return "Esta en el CUARTO cuadrante"

    def vector(self, punto2):
        vector = (punto2.punto()[0]-self.valor_x, punto2.punto()[1]-self.valor_y)
        return vector
    
    def distancia(self, punto2):
        distancia = math.sqrt(((punto2.punto()[0]-self.valor_x)**2)+((punto2.punto()[1]-self.valor_y)**2))
        return distancia    


class Rectangulo():

    def __init__(self, punto1, punto2):
        self.vector = punto1.vector(punto2)

    def base(self):
        base = abs(self.vector[0])
        return base

    def altura(self):
        altura = abs(self.vector[1])
        return altura

    def area(self):
        area = self.base()*self.altura()
        return area

