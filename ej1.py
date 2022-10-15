
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

### Experimentacion ###

# Creacion e impresion de puntos.

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto()

print(A.punto())
print(B.punto())
print(C.punto())
print(D.punto())

# Consultar cuadrantes A, C y D.

AB = A.vector(B)
BA = B.vector(A)

print(AB)
print(BA)

# Consultar la distancia entre los puntos A - B y B - A.

Distancia_A_B = A.distancia(B)
Distancia_B_A = B.distancia(A)

print(Distancia_A_B)
print(Distancia_B_A)

# Determina cual de los tres puntos (A, B, C) se encuentra mas lejos del origen (D).

valores = []
Distancia_A_D = valores.append(A.distancia(D))
Distancia_B_D = valores.append(B.distancia(D))
Distancia_C_D = valores.append(C.distancia(D))
print("El punto que se encuentra a mayor distancia de l origen es el B, con una distancia de:" + str(max(valores)))

# Crea un rectangulo

r = Rectangulo(A,B)

r_base = r.base()
r_altura = r.altura()
r_area = r.area()

print(r_base)
print(r_altura)
print(r_area)

