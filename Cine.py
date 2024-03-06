import Silla as s

class SalaCine:
    def __init__(self, filas=0, columnas=0):
        self.filas = filas
        self.columnas = columnas
        self.mapa_sala = []

    def crear_sala(self):
        pos_silla=1
        for _ in range (1,self.filas+1):
            lista=[]
            for _ in range(1, self.columnas+1):
                lista.append(s.Silla(pos_silla))
                pos_silla+=1
            self.mapa_sala.append(lista)
    
    def mostrarMapaSillas(self):
        for list_sillas in self.mapa_sala:
            for silla in list_sillas:
                print(silla.mostrar_numsilla())

cine = SalaCine(3,4)
cine.crear_sala()
cine.mostrarMapaSillas()
