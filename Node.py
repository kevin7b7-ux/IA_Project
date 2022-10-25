import numpy as np
class Node:
    def __init__(self, entorno):
        self.entorno = entorno
    
    def __str__(self):
        self.mostrar()

    def meta(self,posm,posp):
        if(posm == posp):
            return 1
        else:
            return 0

    def posm(self):
            for i in range(len(self.entorno)):
                for j in range(len(self.entorno[i])):
                    if (self.entorno[i][j]== 3):
                        return [i,j]

    def mostrar(self):
        print("La matriz es la siguiente:")
        for fila in self.entorno:
            for valor in fila:
                print("\t", valor, end=" ")
            print()

    def mover(self, direccion):
        #Copia del entorno
        hijo = np.zeros((len(self.entorno), len(self.entorno[0])))
        for i in range(len(self.entorno)):
            for j in range(len(self.entorno[i])):
                hijo[i][j] = self.entorno[i][j]
                
        # 1->left, 2->Right, 3->Up, 4->Down
        if (direccion == 1):
            for i in range(len(hijo)):
                for j in range(len(hijo[i])):
                    if (hijo[i][j]== 3):
                        hijo[i][j-1]= 3
                        hijo[i][j]= 0
                        return hijo
            return hijo

        if (direccion == 2):
            for i in range(len(hijo)):
                for j in range(len(hijo[i])):
                    if (hijo[i][j]== 3):
                        hijo[i][j+1]= 3
                        hijo[i][j]= 0
                        return hijo
            return hijo

        if (direccion == 3):
            for i in range(len(hijo)):
                for j in range(len(hijo[i])):
                    if (hijo[i][j]== 3):
                        hijo[i-1][j]= 3
                        hijo[i][j]= 0
                        return hijo
            return hijo

        if (direccion == 4):
            for i in range(len(hijo)):
                for j in range(len(hijo[i])):
                    if (hijo[i][j]== 3):
                        hijo[i+1][j]= 3
                        hijo[i][j]= 0
                        return hijo
            return hijo

       
        