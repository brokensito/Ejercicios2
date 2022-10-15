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